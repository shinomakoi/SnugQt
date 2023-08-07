# This is an example that uses the websockets api to know when a prompt execution is done
# Once the prompt execution is done it downloads the images using the /history endpoint

import json
import urllib.parse
import urllib.request
import uuid
from api_args import ApiArgs
import websocket  # NOTE: websocket-client (https://github.com/websocket-client/websocket-client)


class ws_generate:
    def __init__(self):
        server_address = "127.0.0.1:8188"
        client_id = str(uuid.uuid4())

        self.server_address = server_address
        self.client_id = client_id

    def queue_prompt(self, prompt):
        p = {"prompt": prompt, "client_id": self.client_id}
        data = json.dumps(p).encode("utf-8")
        req = urllib.request.Request(
            "http://{}/prompt".format(self.server_address), data=data
        )
        return json.loads(urllib.request.urlopen(req).read())

    def get_image(self, filename, subfolder, folder_type):
        data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
        url_values = urllib.parse.urlencode(data)
        with urllib.request.urlopen(
            "http://{}/view?{}".format(self.server_address, url_values)
        ) as response:
            return response.read()

    def get_history(self, prompt_id):
        with urllib.request.urlopen(
            "http://{}/history/{}".format(self.server_address, prompt_id)
        ) as response:
            return json.loads(response.read())

    def get_images(self, ws, prompt):
        prompt_id = self.queue_prompt(prompt)["prompt_id"]
        output_images = {}
        while True:
            out = ws.recv()
            if isinstance(out, str):
                message = json.loads(out)
                if message["type"] == "executing":
                    data = message["data"]
                    if data["node"] is None and data["prompt_id"] == prompt_id:
                        break  # Execution is done
            else:
                continue  # previews are binary data

        history = self.get_history(prompt_id)[prompt_id]
        for o in history["outputs"]:
            for node_id in history["outputs"]:
                node_output = history["outputs"][node_id]
                if "images" in node_output:
                    images_output = []
                    for image in node_output["images"]:
                        image_data = self.get_image(
                            image["filename"], image["subfolder"], image["type"]
                        )
                        images_output.append(image_data)
                output_images[node_id] = images_output

        return output_images

    ### Get args from api_args.py
    def sd12_preset(self, img_gen_args):
        api_args = ApiArgs()
        prompt = api_args.sd12(img_gen_args)
        return prompt

    def sd12_hires_preset(self, img_gen_args):
        api_args = ApiArgs()
        prompt = api_args.sd12_hires(img_gen_args)
        return prompt

    def sdxl_base_preset(self, img_gen_args):
        api_args = ApiArgs()
        prompt = api_args.sdxl_base(img_gen_args)
        return prompt

    def sdxl_base_refiner_preset(self, img_gen_args):
        api_args = ApiArgs()
        prompt = api_args.sdxl_base_refiner(img_gen_args)
        return prompt

    def img_gen_final(self, img_gen_args):
        """Generate the final image based on the image generation arguments."""
        if img_gen_args["img_gen_preset"] == "sd12":
            prompt = self.sd12_preset(img_gen_args)
        elif img_gen_args["img_gen_preset"] == "sd12_hires":
            prompt = self.sd12_hires_preset(img_gen_args)
        elif img_gen_args["img_gen_preset"] == "sdxl_base":
            prompt = self.sdxl_base_preset(img_gen_args)
        elif img_gen_args["img_gen_preset"] == "sdxl_base_refiner":
            prompt = self.sdxl_base_refiner_preset(img_gen_args)

        ws = websocket.WebSocket()
        ws.connect(f"ws://{self.server_address}/ws?clientId={self.client_id}")
        # print('Comfy JSON Prompt:\n', prompt)
        images = self.get_images(ws, prompt)
        return images
