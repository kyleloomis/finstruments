from finstruments.common.base_enum import BaseEnum


class OptionType(BaseEnum):
    """Option Type"""

    CALL = "CALL"
    PUT = "PUT"


class BarrierType(BaseEnum):
    UP_IN = "UP_IN"
    UP_OUT = "UP_OUT"
    DOWN_IN = "DOWN_IN"
    DOWN_OUT = "DOWN_OUT"


class DoubleBarrierType(BaseEnum):
    KNOCK_IN = "KNOCK_IN"
    KNOCK_OUT = "KNOCK_OUT"
    KNOCK_IN_KNOCK_OUT = "KNOCK_IN_KNOCK_OUT"
    KNOCK_OUT_KNOCK_IN = "KNOCK_OUT_KNOCK_IN"
