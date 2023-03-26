import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.fields as field
from custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.tree import TREE_VARIABLE

class FloatNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Value": field.FLOAT,
            },
        }

    RETURN_TYPES = ("FLOAT",)
    CATEGORY = TREE_VARIABLE
    FUNCTION = "get_value"

    def get_value(self, Value):
        return (Value,)


class IntegerNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Value": field.INT,
            },
        }

    RETURN_TYPES = ("INT",)
    CATEGORY = TREE_VARIABLE
    FUNCTION = "get_value"

    def get_value(self, Value):
        return (Value,)


class StringNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Text": field.STRING,
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_value"
    CATEGORY = TREE_VARIABLE

    def get_value(self, Text):
        return (Text,)


class MultilineStringNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Text": ("STRING", {
                    "default": "",
                    "multiline": True,
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_value"
    CATEGORY = TREE_VARIABLE

    def get_value(self, Text):
        return (Text,)


