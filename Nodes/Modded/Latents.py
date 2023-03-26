import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.fields as field

from custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.tree import TREE_LATENTS
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.sizes as sizes

import math
import torch
import comfy.utils

# DO NOT USE, MAY BREAK ALL
# class EmptyLatentImage:
#     def __init__(self, device="cpu"):
#         self.device = device
#
#     @classmethod
#     def INPUT_TYPES(cls):
#         return {
#             "required": {
#                 "size_tuple": ("TUPLE",),
#                 "batch_size": field.INT,
#             }
#         }
#
#     RETURN_TYPES = ("LATENT",)
#     FUNCTION = "generate"
#     CATEGORY = TREE_LATENTS
#
#     def generate(self, size_tuple, batch_size=1):
#         width = int(size_tuple[0])
#         height = int(size_tuple[1])
#
#         latent = torch.zeros([batch_size, 4, height // 8, width // 8])
#         return ({"samples": latent},)


class LatentScale_Ratio:
    scale_methods = (["nearest-exact", "bilinear", "area"],)
    crop_methods = (["disabled", "center"],)

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent": ("LATENT",),
                "modifier": field.FLOAT,
                "scale_method": cls.scale_methods,
                "crop": cls.crop_methods,
            }
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "scale"
    CATEGORY = TREE_LATENTS

    def scale(self, latent, scale_method, crop, modifier):

        size = sizes.get_latent_size(latent, True)

        lat_width = size[0]
        lat_height = size[1]
        #
        # width = latent["samples"][2]
        # height = latent["samples"][3]

        cls = latent.copy()
        cls["samples"] = comfy.utils.common_upscale(latent["samples"], lat_width // 8, lat_height // 8, scale_method, crop)
        return (cls,)


class LatentScale_Side:
    upscale_methods = ["nearest-exact", "bilinear", "area"]
    crop_methods = ["disabled", "center"]

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent": ("LATENT",),
                "side_length": field.INT,
                "side": (["Width", "Height"],),
                "scale_method": (cls.upscale_methods,),
                "crop": (cls.crop_methods,)}}

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "upscale"

    CATEGORY = TREE_LATENTS

    def upscale(self, latent, side_length, side, scale_method, crop):

        size = sizes.get_latent_size(latent, True)

        lat_width = size[0]
        lat_height = size[1]

        width = lat_width
        height = lat_height

        if side == "Width":
            heigh_ratio = lat_height / lat_width
            width = side_length
            height = heigh_ratio * width
        elif side == "Height":
            width_ratio = lat_width / lat_height
            height = side_length
            width = width_ratio * height

        width = math.ceil(width)
        height = math.ceil(height)

        cls = latent.copy()
        cls["samples"] = comfy.utils.common_upscale(latent["samples"], width // 8, height // 8, scale_method, crop)
        return (cls,)

  # 3rd option with both sides manually

class LatentComposite:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "samples_to": ("LATENT",),
                "samples_from": ("LATENT",),
                "position_tuple": ("TUPLE",),
                "feather": field.INT,
            }
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "compose"
    CATEGORY = TREE_LATENTS

    def compose(self, samples_from, samples_to, position_tuple, feather):
        x_off = int(position_tuple[0] // 8)
        y_off = int(position_tuple[1] // 8)
        feather = feather // 8

        samples_out = samples_to.copy()
        samples = samples_to["samples"].clone()

        samples_to = samples_to["samples"]
        samples_from = samples_from["samples"]

        if feather == 0:
            samples[:, :, y_off:y_off + samples_from.shape[2], x_off:x_off + samples_from.shape[3]] = \
               samples_from[:, :, :samples_to.shape[2] - y_off, :samples_to.shape[3] - x_off]
        else:
            samples_from = samples_from[:, :, :samples_to.shape[2] - y_off, :samples_to.shape[3] - x_off]
            mask = torch.ones_like(samples_from)
            for t in range(feather):
                if y_off != 0:
                    mask[:, :, t:1 + t, :] *= ((1.0 / feather) * (t + 1))

                if y_off + samples_from.shape[2] < samples_to.shape[2]:
                    mask[:, :, mask.shape[2] - 1 - t: mask.shape[2] - t, :] *= ((1.0 / feather) * (t + 1))
                if x_off != 0:
                    mask[:, :, :, t:1 + t] *= ((1.0 / feather) * (t + 1))
                if x_off + samples_from.shape[3] < samples_to.shape[3]:
                    mask[:, :, :, mask.shape[3] - 1 - t: mask.shape[3] - t] *= ((1.0 / feather) * (t + 1))
            rev_mask = torch.ones_like(mask) - mask
            samples[:, :, y_off:y_off + samples_from.shape[2], x_off:x_off + samples_from.shape[3]] = \
                samples_from[:, :, :samples_to.shape[2] - y_off, :samples_to.shape[3] - x_off] * \
                mask + samples[:, :, y_off:y_off + samples_from.shape[2], x_off:x_off + samples_from.shape[3]] *\
                rev_mask
        samples_out["samples"] = samples
        return (samples_out,)