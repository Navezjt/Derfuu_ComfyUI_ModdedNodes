import sys

INT_DEFAULTS = {
    "default": 1,
    "min": -sys.maxsize,
    "max": sys.maxsize
}
FLOAT_DEFAULTS = {
    "default": 1,
    "min": -sys.float_info.max,
    "max": sys.float_info.max,
    "step": 0.01
}
STR_DEFAULTS = {"default": ""}