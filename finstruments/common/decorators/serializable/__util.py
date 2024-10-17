def init_subclass(cls):
    cls._subtypes_[cls.__name__] = cls


def parse_obj(cls, obj):
    return cls._convert_to_real_type_(obj)


def get_validators(cls):
    yield cls._convert_to_real_type_


def convert_to_real_type(cls, data):
    if not isinstance(data, dict):
        return data

    data_type = data.get("descriptor")

    if data_type is None:
        raise ValueError("Missing 'descriptor'")

    searched_types = set()

    def search_for_subtype(cls):
        nonlocal searched_types, data_type

        sub = cls._subtypes_.get(data_type)
        if sub:
            return sub

        searched_types.add(cls)
        for _, sub_type in cls._subtypes_.items():
            if sub_type not in searched_types:
                result = search_for_subtype(sub_type)
                if result:
                    return result
        return None

    sub = search_for_subtype(cls)
    if sub is None:
        raise TypeError(f"Unsupport sub-type: {data_type}")

    return sub(**data)
