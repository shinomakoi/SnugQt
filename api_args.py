import random


class ApiArgs:
    def __init__(self):
        pass

    def sd12(self, img_gen_args):
        ex_vae0 = "16"
        ex_vae1 = 2
        if img_gen_args["sd12_vae"]:
            ex_vae0 = "18"
            ex_vae1 = 0

        api_prompt = {
            "3": {
                "inputs": {
                    "seed": img_gen_args["seed"],
                    "steps": img_gen_args["steps"],
                    "cfg": img_gen_args["cfg"],
                    "sampler_name": img_gen_args["sampler_name"],
                    "scheduler": img_gen_args["scheduler"],
                    "denoise": 1,
                    "model": ["16", 0],
                    "positive": ["6", 0],
                    "negative": ["7", 0],
                    "latent_image": ["5", 0],
                },
                "class_type": "KSampler",
            },
            "5": {
                "inputs": {
                    "width": img_gen_args["width"],
                    "height": img_gen_args["height"],
                    "batch_size": img_gen_args["batch_size"],
                },
                "class_type": "EmptyLatentImage",
            },
            "6": {
                "inputs": {"text": img_gen_args["pos_prompt"], "clip": ["16", 1]},
                "class_type": "CLIPTextEncode",
            },
            "7": {
                "inputs": {"text": img_gen_args["neg_prompt"], "clip": ["16", 1]},
                "class_type": "CLIPTextEncode",
            },
            "12": {
                "inputs": {
                    "filename_prefix": img_gen_args["filename_prefix"],
                    "images": ["13", 0],
                },
                "class_type": "SaveImage",
            },
            "13": {
                "inputs": {"samples": ["3", 0], "vae": [ex_vae0, ex_vae1]},
                "class_type": "VAEDecode",
            },
            "16": {
                "inputs": {"ckpt_name": img_gen_args["sd12_ckpt"]},
                "class_type": "CheckpointLoaderSimple",
            },
            "18": {
                "inputs": {"vae_name": img_gen_args["sd12_vae"]},
                "class_type": "VAELoader",
            },
        }
        return api_prompt

    def sd12_hires(self, img_gen_args):
        ex_vae0 = "16"
        ex_vae1 = 2
        if img_gen_args["sd12_vae"]:
            ex_vae0 = "18"
            ex_vae1 = 0

        api_prompt = {
            "3": {
                "inputs": {
                    "seed": img_gen_args["seed"],
                    "steps": img_gen_args["steps"],
                    "cfg": img_gen_args["cfg"],
                    "sampler_name": img_gen_args["sampler_name"],
                    "scheduler": img_gen_args["scheduler"],
                    "denoise": 1,
                    "model": ["16", 0],
                    "positive": ["6", 0],
                    "negative": ["7", 0],
                    "latent_image": ["5", 0],
                },
                "class_type": "KSampler",
            },
            "5": {
                "inputs": {
                    "width": img_gen_args["width"],
                    "height": img_gen_args["height"],
                    "batch_size": img_gen_args["batch_size"],
                },
                "class_type": "EmptyLatentImage",
            },
            "6": {
                "inputs": {"text": img_gen_args["pos_prompt"], "clip": ["16", 1]},
                "class_type": "CLIPTextEncode",
            },
            "7": {
                "inputs": {"text": img_gen_args["neg_prompt"], "clip": ["16", 1]},
                "class_type": "CLIPTextEncode",
            },
            "11": {
                "inputs": {
                    "seed": random.randint(1, 4294967294),
                    "steps": img_gen_args["hiresfix_steps"],
                    "cfg": img_gen_args["cfg"],
                    "sampler_name": img_gen_args["sampler_name"],
                    "scheduler": img_gen_args["scheduler"],
                    "denoise": 0.55,
                    "model": ["16", 0],
                    "positive": ["6", 0],
                    "negative": ["7", 0],
                    "latent_image": ["17", 0],
                },
                "class_type": "KSampler",
            },
            "12": {
                "inputs": {
                    "filename_prefix": img_gen_args["filename_prefix"],
                    "images": ["13", 0],
                },
                "class_type": "SaveImage",
            },
            "13": {
                "inputs": {"samples": ["11", 0], "vae": [ex_vae0, ex_vae1]},
                "class_type": "VAEDecode",
            },
            "16": {
                "inputs": {"ckpt_name": img_gen_args["sd12_ckpt"]},
                "class_type": "CheckpointLoaderSimple",
            },
            "17": {
                "inputs": {
                    "upscale_method": "nearest-exact",
                    "scale_by": img_gen_args["hiresfix_scale_by"],
                    "samples": ["3", 0],
                },
                "class_type": "LatentUpscaleBy",
            },
            "18": {
                "inputs": {"vae_name": img_gen_args["sd12_vae"]},
                "class_type": "VAELoader",
            },
        }
        return api_prompt

    def sdxl_base(self, img_gen_args):
        ex_vae0 = "4"
        ex_vae1 = 2
        if img_gen_args["sdxl_vae"]:
            ex_vae0 = "51"
            ex_vae1 = 0

        api_prompt = {
            "4": {
                "inputs": {"ckpt_name": img_gen_args["sdxl_base_ckpt"]},
                "class_type": "CheckpointLoaderSimple",
            },
            "5": {
                "inputs": {
                    "width": img_gen_args["width"],
                    "height": img_gen_args["height"],
                    "batch_size": img_gen_args["batch_size"],
                },
                "class_type": "EmptyLatentImage",
            },
            "6": {
                "inputs": {"text": img_gen_args["pos_prompt"], "clip": ["4", 1]},
                "class_type": "CLIPTextEncode",
            },
            "7": {
                "inputs": {"text": img_gen_args["neg_prompt"], "clip": ["4", 1]},
                "class_type": "CLIPTextEncode",
            },
            "17": {
                "inputs": {"samples": ["50", 0], "vae": [ex_vae0, ex_vae1]},
                "class_type": "VAEDecode",
            },
            "19": {
                "inputs": {
                    "filename_prefix": img_gen_args["filename_prefix"],
                    "images": ["17", 0],
                },
                "class_type": "SaveImage",
            },
            "50": {
                "inputs": {
                    "seed": img_gen_args["seed"],
                    "steps": img_gen_args["steps"],
                    "cfg": img_gen_args["cfg"],
                    "sampler_name": img_gen_args["sampler_name"],
                    "scheduler": img_gen_args["scheduler"],
                    "denoise": 1,
                    "model": ["4", 0],
                    "positive": ["6", 0],
                    "negative": ["7", 0],
                    "latent_image": ["5", 0],
                },
                "class_type": "KSampler",
            },
            "51": {
                "inputs": {"vae_name": img_gen_args["sdxl_vae"]},
                "class_type": "VAELoader",
            },
        }
        return api_prompt

    def sdxl_base_refiner(self, img_gen_args):
        ex_vae0 = "4"
        ex_vae1 = 2
        if img_gen_args["sdxl_vae"]:
            ex_vae0 = "50"
            ex_vae1 = 0

        total_steps = int(img_gen_args["steps"]) + int(
            img_gen_args["sdxl_refiner_steps"]
        )

        api_prompt = {
            "4": {
                "inputs": {"ckpt_name": img_gen_args["sdxl_base_ckpt"]},
                "class_type": "CheckpointLoaderSimple",
            },
            "5": {
                "inputs": {
                    "width": img_gen_args["width"],
                    "height": img_gen_args["height"],
                    "batch_size": img_gen_args["batch_size"],
                },
                "class_type": "EmptyLatentImage",
            },
            "6": {
                "inputs": {"text": img_gen_args["pos_prompt"], "clip": ["4", 1]},
                "class_type": "CLIPTextEncode",
            },
            "7": {
                "inputs": {"text": img_gen_args["neg_prompt"], "clip": ["4", 1]},
                "class_type": "CLIPTextEncode",
            },
            "10": {
                "inputs": {
                    "add_noise": "enable",
                    "noise_seed": img_gen_args["seed"],
                    "steps": total_steps,
                    "cfg": img_gen_args["cfg"],
                    "sampler_name": img_gen_args["sampler_name"],
                    "scheduler": img_gen_args["scheduler"],
                    "start_at_step": 0,
                    "end_at_step": img_gen_args["steps"],
                    "return_with_leftover_noise": "enable",
                    "model": ["4", 0],
                    "positive": ["6", 0],
                    "negative": ["7", 0],
                    "latent_image": ["5", 0],
                },
                "class_type": "KSamplerAdvanced",
            },
            "11": {
                "inputs": {
                    "add_noise": "disable",
                    "noise_seed": random.randint(1, 4294967294),
                    "steps": total_steps,
                    "cfg": img_gen_args["cfg"],
                    "sampler_name": img_gen_args["sampler_name"],
                    "scheduler": img_gen_args["scheduler"],
                    "start_at_step": img_gen_args["steps"],
                    "end_at_step": 10000,
                    "return_with_leftover_noise": "disable",
                    "model": ["12", 0],
                    "positive": ["15", 0],
                    "negative": ["16", 0],
                    "latent_image": ["10", 0],
                },
                "class_type": "KSamplerAdvanced",
            },
            "12": {
                "inputs": {"ckpt_name": img_gen_args["sdxl_refiner_ckpt"]},
                "class_type": "CheckpointLoaderSimple",
            },
            "15": {
                "inputs": {"text": img_gen_args["pos_prompt"], "clip": ["12", 1]},
                "class_type": "CLIPTextEncode",
            },
            "16": {
                "inputs": {"text": img_gen_args["neg_prompt"], "clip": ["12", 1]},
                "class_type": "CLIPTextEncode",
            },
            "17": {
                "inputs": {"samples": ["11", 0], "vae": [ex_vae0, ex_vae1]},
                "class_type": "VAEDecode",
            },
            "19": {
                "inputs": {
                    "filename_prefix": img_gen_args["filename_prefix"],
                    "images": ["17", 0],
                },
                "class_type": "SaveImage",
            },
            "50": {
                "inputs": {"vae_name": img_gen_args["sdxl_vae"]},
                "class_type": "VAELoader",
            },
        }
        return api_prompt
