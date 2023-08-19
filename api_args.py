import random


class ApiArgs:
    def __init__(self):
        pass

    def so_upscale(self, img_gen_args):
        prompt = {
            "1": {
                "inputs": {
                    "image": img_gen_args["so_upscale_image"],
                    "choose file to upload": "image",
                },
                "class_type": "LoadImage",
            },
            "2": {
                "inputs": {"model_name": img_gen_args["so_upscale_model"]},
                "class_type": "UpscaleModelLoader",
            },
            "3": {
                "inputs": {"upscale_model": ["2", 0], "image": ["1", 0]},
                "class_type": "ImageUpscaleWithModel",
            },
            "4": {
                "inputs": {"filename_prefix": "SnugQt/SnugQt", "images": ["5", 0]},
                "class_type": "SaveImage",
            },
        }

        if img_gen_args["downscale"]:
            downscale_node = {
                "inputs": {
                    "upscale_method": "bicubic",
                    "scale_by": img_gen_args["downscale"],
                    "image": ["3", 0],
                },
                "class_type": "ImageScaleBy",
            }
            prompt["5"] = downscale_node
        print(prompt)

        return prompt

    def gen_base(self, img_gen_args):
        base_node = {
            "1": {
                "inputs": {"ckpt_name": img_gen_args["ckpt_name"]},
                "class_type": "CheckpointLoaderSimple",
            },
            "4": {
                "inputs": {"text": img_gen_args["pos_prompt"], "clip": ["1", 1]},
                "class_type": "CLIPTextEncode",
            },
            "5": {
                "inputs": {"text": img_gen_args["neg_prompt"], "clip": ["1", 1]},
                "class_type": "CLIPTextEncode",
            },
            "6": {
                "inputs": {
                    "width": img_gen_args["width"],
                    "height": img_gen_args["height"],
                    "batch_size": img_gen_args["batch_size"],
                },
                "class_type": "EmptyLatentImage",
            },
            "7": {
                "inputs": {
                    "seed": img_gen_args["seed"],
                    "steps": img_gen_args["steps"],
                    "cfg": img_gen_args["cfg"],
                    "sampler_name": img_gen_args["sampler_name"],
                    "scheduler": img_gen_args["scheduler"],
                    "denoise": 1.0,
                    "model": ["1", 0],
                    "positive": ["4", 0],
                    "negative": ["5", 0],
                    "latent_image": ["6", 0],
                },
                "class_type": "KSampler",
            },
            "10": {
                "inputs": {"samples": ["7", 0], "vae": ["1", 2]},
                "class_type": "VAEDecode",
            },
            "11": {
                "inputs": {
                    "filename_prefix": img_gen_args["filename_prefix"],
                    "images": ["10", 0],
                },
                "class_type": "SaveImage",
            },
            "12": {
                "inputs": {
                    "stop_at_clip_layer": img_gen_args["clip_skip"],
                    "clip": ["1", 1],
                },
                "class_type": "CLIPSetLastLayer",
            },
        }
        return base_node

    def gen_external_vae(self, img_gen_args):
        ex_vae_node = {
            "inputs": {"vae_name": img_gen_args["external_vae"]},
            "class_type": "VAELoader",
        }
        return ex_vae_node

    def gen_lora(self, img_gen_args):
        lora_node = {
            "inputs": {
                "lora_name": img_gen_args["lora"],
                "strength_model": img_gen_args["lora_strength"],
                "strength_clip": img_gen_args["lora_clip_strength"],
                "model": ["1", 0],
                "clip": ["1", 1],
            },
            "class_type": "LoraLoader",
        }
        return lora_node

    def gen_hires_fix(self, img_gen_args):
        node1 = {
            "inputs": {
                "upscale_method": "nearest-exact",
                "scale_by": img_gen_args["hiresfix_scale_by"],
                "samples": ["7", 0],
            },
            "class_type": "LatentUpscaleBy",
        }

        node2 = {
            "inputs": {
                "seed": random.randint(1, 4294967294),
                "steps": img_gen_args["hiresfix_steps"],
                "cfg": img_gen_args["cfg"],
                "sampler_name": img_gen_args["sampler_name"],
                "scheduler": img_gen_args["scheduler"],
                "denoise": img_gen_args["hiresfix_denoise"],
                "model": ["1", 0],
                "positive": ["4", 0],
                "negative": ["5", 0],
                "latent_image": ["8", 0],
            },
            "class_type": "KSampler",
        }
        return node1, node2

    def gen_refiner_node(self, img_gen_args):
        total_steps = int(img_gen_args["steps"]) + int(
            img_gen_args["sdxl_refiner_steps"]
        )

        refiner_model = {
            "inputs": {"ckpt_name": img_gen_args["sdxl_refiner_ckpt"]},
            "class_type": "CheckpointLoaderSimple",
        }

        refiner_node = {
            "inputs": {
                "add_noise": "disable",
                "noise_seed": 0,
                "steps": total_steps,
                "cfg": img_gen_args["cfg"],
                "sampler_name": img_gen_args["sampler_name"],
                "scheduler": img_gen_args["scheduler"],
                "start_at_step": img_gen_args["steps"],
                "end_at_step": 10000,
                "return_with_leftover_noise": "disable",
                "model": ["98", 0],
                "positive": ["96", 0],
                "negative": ["97", 0],
                "latent_image": ["7", 0],
            },
            "class_type": "KSamplerAdvanced",
        }

        pos_clip = {
            "inputs": {"text": img_gen_args["pos_prompt"], "clip": ["98", 1]},
            "class_type": "CLIPTextEncode",
        }
        neg_clip = {
            "inputs": {
                "text": img_gen_args["neg_prompt"],
                "clip": ["98", 1],
            },
            "class_type": "CLIPTextEncode",
        }
        return refiner_model, refiner_node, pos_clip, neg_clip

    def gen_upscale_model(self, img_gen_args):
        node1 = {
            "inputs": {"model_name": img_gen_args["upscale_model"]},
            "class_type": "UpscaleModelLoader",
        }
        node2 = {
            "inputs": {"upscale_model": ["16", 0], "image": ["10", 0]},
            "class_type": "ImageUpscaleWithModel",
        }
        return node1, node2

    def gen_img2img(self, img_gen_args):
        LoadImage = {
            "inputs": {
                "image": img_gen_args["img2img_load"],
                "choose file to upload": "image",
            },
            "class_type": "LoadImage",
        }
        VAEEncode = {
            "inputs": {"pixels": ["80", 0], "vae": ["1", 2]},
            "class_type": "VAEEncode",
        }
        return LoadImage, VAEEncode

    def gen_inpainting(self, img_gen_args):
        LoadImage = {
            "inputs": {
                "image": str(img_gen_args["inpainting_load"]),
                "choose file to upload": "image",
            },
            "class_type": "LoadImage",
        }
        VAEEncode = {
            "inputs": {
                "grow_mask_by": 18,
                "pixels": ["80", 0],
                "vae": ["1", 2],
                "mask": ["80", 1],
            },
            "class_type": "VAEEncodeForInpaint",
        }
        return LoadImage, VAEEncode

    def generate_api_prompt(self, img_gen_args):
        api_prompt = self.gen_base(img_gen_args)

        if img_gen_args["external_vae"]:
            ex_vae_node = self.gen_external_vae(img_gen_args)
            api_prompt["2"] = ex_vae_node
            api_prompt["10"]["inputs"]["vae"][0] = "2"
            api_prompt["10"]["inputs"]["vae"][1] = 0

        if img_gen_args["lora"]:
            lora_node = self.gen_lora(img_gen_args)
            api_prompt["3"] = lora_node
            api_prompt["4"]["inputs"]["clip"][0] = "3"
            api_prompt["5"]["inputs"]["clip"][0] = "3"
            api_prompt["7"]["inputs"]["model"][0] = "3"

        if (
            img_gen_args["hiresfix_steps"]
            and not img_gen_args["sdxl_refiner_ckpt"]
            and not img_gen_args["img2img_load"]
            and not img_gen_args["inpainting_load"]
        ):
            node1, node2 = self.gen_hires_fix(img_gen_args)
            api_prompt["8"] = node1
            api_prompt["9"] = node2
            api_prompt["10"]["inputs"]["samples"][0] = "9"
            if img_gen_args["lora"]:
                api_prompt["9"]["inputs"]["model"][0] = "3"

        if img_gen_args["upscale_model"]:
            node1, node2 = self.gen_upscale_model(img_gen_args)
            api_prompt["16"] = node1
            api_prompt["17"] = node2
            api_prompt["11"]["inputs"]["images"][0] = "17"

        if img_gen_args["sdxl_refiner_ckpt"]:
            refiner_model, refiner_node, pos_clip, neg_clip = self.gen_refiner_node(
                img_gen_args
            )
            api_prompt["98"] = refiner_model
            api_prompt["99"] = refiner_node
            api_prompt["96"] = pos_clip
            api_prompt["97"] = neg_clip
            api_prompt["10"]["inputs"]["samples"][0] = "99"

        if img_gen_args["img2img_load"]:
            LoadImage, VAEEncode = self.gen_img2img(img_gen_args)
            api_prompt["80"] = LoadImage
            api_prompt["81"] = VAEEncode
            api_prompt["7"]["inputs"]["latent_image"][0] = "81"
            api_prompt["7"]["inputs"]["denoise"] = img_gen_args["img2img_denoise"]
            if img_gen_args["external_vae"]:
                api_prompt["81"]["inputs"]["vae"][0] = "2"
                api_prompt["81"]["inputs"]["vae"][1] = 0

        if img_gen_args["inpainting_load"]:
            LoadImage, VAEEncode = self.gen_inpainting(img_gen_args)
            api_prompt["80"] = LoadImage
            api_prompt["81"] = VAEEncode
            api_prompt["7"]["inputs"]["latent_image"][0] = "81"
            api_prompt["7"]["inputs"]["denoise"] = img_gen_args["inpaint_denoise"]
            if img_gen_args["external_vae"]:
                api_prompt["81"]["inputs"]["vae"][0] = "2"
                api_prompt["81"]["inputs"]["vae"][1] = 0

        return api_prompt
