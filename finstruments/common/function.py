"""
Helper functions.
"""


def to_nested_dict(data, separator="."):
    """
    This method takes a dict and splits keys by the seperator to create a nested dict

    Parameters:
        data: dict to unwind into a nested dict
        separator: seperator used to split keys to build the nested dict

    Returns:
        A nested dict
    """
    nested_dict = {}
    for key, value in data.items():
        keys = key.split(separator)
        d = nested_dict
        for subkey in keys[:-1]:
            if subkey not in d:
                d[subkey] = {}
            d = d[subkey]
        d[keys[-1]] = value
    return nested_dict
