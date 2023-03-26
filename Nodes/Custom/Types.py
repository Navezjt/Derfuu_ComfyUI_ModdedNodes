import math
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.DEFAULTS_VALUES as DEFVAL
from custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.tree import TREE_VARIABLE



class FloatNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # "VALUE": field.FLOAT,
                "VALUE": ("FLOAT", DEFVAL.FLOAT_DEFAULTS),
            },
        }

    # RETURN_TYPES = (type.FLOAT,)
    RETURN_TYPES = ("FLOAT",)
    CATEGORY = TREE_VARIABLE
    FUNCTION = "get_value"

    def get_value(self, VALUE):
        return (VALUE,)


class IntegerNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "VALUE": ("INT", DEFVAL.INT_DEFAULTS),
            },
        }

    RETURN_TYPES = ("INT",)
    CATEGORY = TREE_VARIABLE
    FUNCTION = "get_value"

    def get_value(self, VALUE):
        return (VALUE,)

class TupleNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "FLOAT_A": ("FLOAT", DEFVAL.FLOAT_DEFAULTS),
                "FLOAT_B": ("FLOAT", DEFVAL.FLOAT_DEFAULTS),
                "Ceil2Int": ([False, True],),
            }
        }

    RETURN_TYPES = ("TUPLE",)
    CATEGORY = TREE_VARIABLE

    FUNCTION = 'get_value'

    def get_value(self, FLOAT_A, FLOAT_B, Ceil2Int="false"):
        if Ceil2Int == "true":
            FLOAT_A = math.ceil(FLOAT_A)
            FLOAT_B = math.ceil(FLOAT_B)
        return ((FLOAT_A, FLOAT_B),)


class StringNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "VALUE": ("STRING", DEFVAL.STR_DEFAULTS),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_value"
    CATEGORY = TREE_VARIABLE

    def get_value(self, VALUE):
        return (VALUE,)
#
#
# class MultilineStringNode:
#     def __init__(self):
#         pass
#
#     @classmethod
#     def INPUT_TYPES(cls):
#         return {
#             "required": {
#                 "VALUE": field.STRING_ML,
#             }
#         }
#
#     RETURN_TYPES = (type.STRING,)
#     FUNCTION = "get_value"
#     CATEGORY = TREE_VARIABLE
#
#     def get_value(self, VALUE):
#         return (VALUE,)
#
#
