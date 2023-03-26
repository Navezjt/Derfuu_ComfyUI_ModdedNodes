import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.types as type

import math

from custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.tree import TREE_CONVERTERS


class Int2Float:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "NodeINT": (type.NodeINT,),
            }
        }

    RETURN_TYPES = (type.FLOAT,)
    FUNCTION = "get_value"
    CATEGORY = TREE_CONVERTERS

    def get_value(self, INT):
        return (float(INT),)


class CeilNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "FLOAT": (type.FLOAT,),
            }
        }

    RETURN_TYPES = (type.NodeINT,)
    FUNCTION = "get_value"
    CATEGORY = TREE_CONVERTERS

    def get_value(self, FLOAT):
        total = int(math.ceil(FLOAT))
        return (total,)


class FloorNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "FLOAT": (type.FLOAT,),
            }
        }

    RETURN_TYPES = (type.NodeINT,)
    FUNCTION = "get_value"
    CATEGORY = TREE_CONVERTERS

    def get_value(self, FLOAT):
        total = int(math.floor(FLOAT))
        return (total,)


class ABSNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "FLOAT": (type.FLOAT,),
                "IsNegative": ([False, True],)
            }
        }

    RETURN_TYPES = (type.FLOAT,)
    FUNCTION = "abs_val"
    CATEGORY = TREE_CONVERTERS

    def abs_val(self, FLOAT, IsNegative):
        if IsNegative:
            return (-abs(FLOAT),)
        return (abs(FLOAT),)


class Modd2Orig:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "mod_INT": (type.NodeINT,),
            }
        }

    RETURN_TYPES = (type.OrigINT,)
    FUNCTION = "conv"
    CATEGORY = TREE_CONVERTERS

    def conv(self, mod_INT):
        return (mod_INT,)


class Orig2Modd:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "orig_INT": (type.OrigINT,),
            }
        }

    RETURN_TYPES = (type.NodeINT,)
    FUNCTION = "conv"
    CATEGORY = TREE_CONVERTERS

    def conv(self, orig_INT):
        return (orig_INT,)