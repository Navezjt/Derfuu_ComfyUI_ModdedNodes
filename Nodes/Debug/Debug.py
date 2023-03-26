import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.types as type
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.fields as field

import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.DEFAULTS_VALUES as DEFVAL

from custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.tree import TREE_DEBUG

class DebugNodeFloat:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TITLE": ("STRING", DEFVAL.STR_DEFAULTS),
                "FLOAT": ("FLOAT", DEFVAL.FLOAT_DEFAULTS)
            }
        }

    RETURN_TYPES = ()
    CATEGORY = TREE_DEBUG
    FUNCTION = "print_values"
    OUTPUT_NODE = True

    def print_values(self, FLOAT, TITLE):
        print(f"{TITLE}: {FLOAT}", sep="\n")
        return (None,)


class DebugNodeInt:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TITLE": ("STRING", DEFVAL.STR_DEFAULTS),
                "INT": ("INT", DEFVAL.INT_DEFAULTS)
            }
        }

    RETURN_TYPES = ()
    CATEGORY = TREE_DEBUG
    FUNCTION = "print_values"
    OUTPUT_NODE = True

    def print_values(self, INT, TITLE):
        print(f"{TITLE}: {INT}", sep="\n")
        return (None,)


class DebugNodeTuple:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TITLE": ("STRING", DEFVAL.STR_DEFAULTS),
                "TUPLE": ("TUPLE",),
            }
        }

    RETURN_TYPES = ()
    CATEGORY = TREE_DEBUG
    FUNCTION = "print_values"
    OUTPUT_NODE = True

    def print_values(self, TUPLE, TITLE):
        print(f"{TITLE}: {TUPLE}", sep="\n")
        return (None,)

class DebugNodeString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TITLE": field.STRING,
                "STRING": (type.STRING,),
            }
        }

    RETURN_TYPES = ()
    CATEGORY = TREE_DEBUG
    FUNCTION = "print_values"
    OUTPUT_NODE = True

    def print_values(self, STRING, TITLE):
        print(f"{TITLE}: {STRING}", sep="\n")
        return (None,)