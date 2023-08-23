import glob
import platform
import random
import sys
import tempfile
from datetime import datetime
from pathlib import Path

import yaml
from PySide6 import QtWidgets
from PySide6.QtCore import QSize, QThread, Signal, Slot
from PySide6.QtGui import QIcon, QImage, QPixmap
from PySide6.QtWidgets import QApplication, QFileDialog, QMenu
from qt_material import apply_stylesheet

from comfy_api_fetch import ws_generate
from inpaint_window import InpaintMaskEditor
from main_window import Ui_MainWindow
from settings_window import Ui_SettingsDialog

SETTINGS_FILE = Path("settings.yaml")
DEFAULT_SETTINGS_FILE = Path("assets/default_settings.yaml")
STYLES_FILE = Path("assets/styles.yaml")
APP_ICON = Path("assets/appicon.png")


class RunAPI(QThread):
    final_resultReady = Signal(list, bool, int)

    def __init__(
        self,
        img_gen_args: dict,
        tab_index: int,
    ):
        super().__init__()
        self.img_gen_args = img_gen_args
        self.tab_index = tab_index
        self.temp_image_list = []

    # Launcher of SD gen or upscale
    def run(self):
        if self.img_gen_args:
            try:
                self.upscale_gen() if self.img_gen_args[
                    "so_upscale_model"
                ] else self.img_gen()
            except Exception as error:
                self.final_resultReady.emit(None, False, None)
                print("--- Error during generation:\n", error)
                return

    def upscale_gen(self):
        img_fetch = ws_generate()

        def generate_image_list(images):
            return [image_data for node_id in images for image_data in images[node_id]]

        images = img_fetch.img_gen_final(self.img_gen_args)
        self.temp_image_list.extend(generate_image_list(images))

        # Check if no images were generated
        if not self.temp_image_list:
            print("--- No images were generated")
            self.final_resultReady.emit(None, False, None)

        self.final_resultReady.emit(self.temp_image_list, True, self.tab_index)

    # Generate the image and emit the final result
    def img_gen(self):
        img_fetch = ws_generate()

        # Use a boolean expression instead of comparing to a string
        random_seed = self.img_gen_args["seed"] == "random"

        # Define a helper function to generate an image list from a dictionary of images
        def generate_image_list(images):
            return [image_data for node_id in images for image_data in images[node_id]]

        # Generate images for the specified number of iterations
        for loop in range(self.img_gen_args["iterations"]):
            # Set the seed to a random value if random_seed is True
            if random_seed:
                self.img_gen_args["seed"] = random.randint(1, 4294967294)
            # Generate the images and add them to the image list
            images = img_fetch.img_gen_final(self.img_gen_args)
            self.temp_image_list.extend(generate_image_list(images))
            # Increment the seed if random_seed is False
            if not random_seed:
                self.img_gen_args["seed"] += 1

        # Check if no images were generated
        if not self.temp_image_list:
            print("--- No images were generated")
            self.final_resultReady.emit(None, False, None)

        self.final_resultReady.emit(self.temp_image_list, True, self.tab_index)


class SettingsWindow(QtWidgets.QWidget, Ui_SettingsDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Set the window icon
        icon = QIcon()
        icon.addFile(str(APP_ICON), QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.comfyuiModelFolderSelect.clicked.connect(self.comfyui_model_folder_select)
        self.comfyuiExtraFolderSelect.clicked.connect(self.comfyui_extra_folder_select)

        self.saveSettingsButton.clicked.connect(self.save_settings)
        self.reloadModelsButton.clicked.connect(self.add_models)

        self.load_settings()

    def get_directory_path(self, title):
        directory_path = str(QFileDialog.getExistingDirectory(self, title))
        return directory_path

    # Load settings from settings.yaml
    def load_settings(self):
        read_file = SETTINGS_FILE if SETTINGS_FILE.is_file() else DEFAULT_SETTINGS_FILE
        with open(read_file, "r") as stream:
            data = yaml.safe_load(stream)

            # Checkpoints
            checkpoints = data["checkpoints"]
            self.comfyuiModelFolderValue.setText(checkpoints["comfy_model_folder"])
            self.comfyuiExtraFolderValue.setText(
                checkpoints["comfy_extra_model_folder"]
            )
            self.add_models()
            self.checkpointCombo.setCurrentText(checkpoints["checkpoint"])
            self.sdxlRefinerCheckpointCombo.setCurrentText(checkpoints["sdxl_refiner"])
            self.externalVaeCombo.setCurrentText(checkpoints["external_vae"])
            self.modelUpscaleCombo.setCurrentText(checkpoints["upscale_model"])
            self.useExternalVaeCheck.setChecked(checkpoints["use_ex_vae"])
            # Parameters
            params = data["parameters"]
            self.imgWidthValue.setValue(params["width"])
            self.imgHeightValue.setValue(params["height"])
            self.seedValue.setValue(params["seed"])
            self.batchValue.setValue(params["batch_size"])
            self.iterationsValue.setValue(params["iterations"])
            self.cfgValue.setValue(params["cfg"])
            self.stepsValue.setValue(params["steps"])
            self.sdxlRefinerCheck.setChecked(params["sdxl_refiner"])
            self.sdxlRefinerStepsValue.setValue(params["sdxl_refiner_steps"])
            self.samplerValue.setCurrentText(params["sampler"])
            self.schedulerValue.setCurrentText(params["scheduler"])
            self.modelUpscaleCheck.setChecked(params["model_upscale"])
            # Lora
            lora = data["lora"]
            self.loraCheck.setChecked(lora["use"])
            self.loraCombo.setCurrentText(lora["lora_file"])
            self.loraStrengthSpin.setValue(lora["model_strength"])
            self.loraClipStrengthSpin.setValue(lora["clip_strength"])
            # Preferences
            preferences = data["preferences"]
            self.keepImagesCheck.setChecked(preferences["keep_images"])
            self.maxImagesSpin.setValue(preferences["max_images"])

    # Save settings to settings.yaml
    def save_settings(self):
        read_file = SETTINGS_FILE if SETTINGS_FILE.is_file() else DEFAULT_SETTINGS_FILE
        with open(read_file, "r") as stream:
            data = yaml.safe_load(stream)
            # Checkpoints
            data["checkpoints"].update(
                {
                    "comfy_model_folder": self.comfyuiModelFolderValue.text(),
                    "comfy_extra_model_folder": self.comfyuiExtraFolderValue.text(),
                    "checkpoint": self.checkpointCombo.currentText(),
                    "sdxl_refiner": self.sdxlRefinerCheckpointCombo.currentText(),
                    "external_vae": self.externalVaeCombo.currentText(),
                    "use_ex_vae": self.useExternalVaeCheck.isChecked(),
                    "upscale_model": self.modelUpscaleCombo.currentText(),
                }
            )
            # Parameters
            data["parameters"].update(
                {
                    "width": self.imgWidthValue.value(),
                    "height": self.imgHeightValue.value(),
                    "seed": self.seedValue.value(),
                    "batch_size": self.batchValue.value(),
                    "iterations": self.iterationsValue.value(),
                    "cfg": self.cfgValue.value(),
                    "steps": self.stepsValue.value(),
                    "sdxl_refiner": self.sdxlRefinerCheck.isChecked(),
                    "sdxl_refiner_steps": self.sdxlRefinerStepsValue.value(),
                    "sampler": self.samplerValue.currentText(),
                    "scheduler": self.schedulerValue.currentText(),
                    "model_upscale": self.modelUpscaleCheck.isChecked(),
                }
            )
            # Lora
            data["lora"].update(
                {
                    "use": self.loraCheck.isChecked(),
                    "lora_file": self.loraCombo.currentText(),
                    "model_strength": self.loraStrengthSpin.value(),
                    "clip_strength": self.loraClipStrengthSpin.value(),
                }
            )
            data["preferences"].update(
                {
                    "keep_images": self.keepImagesCheck.isChecked(),
                    "max_images": self.maxImagesSpin.value(),
                }
            )

        with open(SETTINGS_FILE, "w") as stream:
            yaml.dump(data, stream, default_flow_style=False)
        print("Settings saved")

    # Add the model names to the combo boxes
    def add_models(self):
        # Add ckpts
        ckpts = sorted(
            [
                Path(ckpt).name
                for extension in ("*.safetensors", "*.ckpt")
                for ckpt in glob.glob(
                    f"{self.comfyuiModelFolderValue.text()}/checkpoints/{extension}"
                )
            ]
        )
        extra_ckpts = sorted(
            [
                Path(extra_ckpt).name
                for extension in ("*.safetensors", "*.ckpt")
                for extra_ckpt in glob.glob(
                    f"{self.comfyuiExtraFolderValue.text()}/{extension}"
                )
            ]
        )
        for combo in (
            self.checkpointCombo,
            self.sdxlRefinerCheckpointCombo,
        ):
            combo.clear()
            combo.addItems(ckpts)
            combo.addItems(extra_ckpts)
        print("--- Added checkpoints:", ckpts, extra_ckpts)

        # Add VAEs
        vaes = sorted(
            [
                Path(vae).name
                for extension in ("*.safetensors", "*.ckpt")
                for vae in glob.glob(
                    f"{self.comfyuiModelFolderValue.text()}/vae/{extension}"
                )
            ]
        )
        self.externalVaeCombo.clear()
        self.externalVaeCombo.addItems(vaes)
        print("--- Added VAEs:", vaes)

        # Add LoRAs
        loras = sorted(
            [
                Path(lora).name
                for extension in ("*.safetensors", "*.ckpt")
                for lora in glob.glob(
                    f"{self.comfyuiModelFolderValue.text()}/loras/{extension}"
                )
            ]
        )
        self.loraCombo.clear()
        self.loraCombo.addItems(loras)
        print("--- Added LoRAs:", loras)

        # Add upscale models
        upscale_models = sorted(
            [
                Path(upscale_model).name
                for extension in ("*.pth", "*.onnx")
                for upscale_model in glob.glob(
                    f"{self.comfyuiModelFolderValue.text()}/upscale_models/{extension}"
                )
            ]
        )
        self.modelUpscaleCombo.clear()
        self.modelUpscaleCombo.addItems(upscale_models)
        print("--- Added upscale models:", upscale_models)

    # Browse for ComfyUI model folder
    def comfyui_model_folder_select(self):
        model_folder = self.get_directory_path("Select ComfyUI model directory")
        if model_folder:
            self.comfyuiModelFolderValue.setText(model_folder)
            self.add_models()

    # Browse for ComfyUI extra models folder
    def comfyui_extra_folder_select(self):
        extra_model_folder = self.get_directory_path(
            "Select ComfyUI extra checkpoint directory"
        )
        if extra_model_folder:
            self.comfyuiExtraFolderValue.setText(extra_model_folder)
            self.add_models()


class MagiApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Set the window icon
        icon = QIcon()
        icon.addFile(str(APP_ICON), QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.settings_win = SettingsWindow()
        self.statusbar.showMessage("Status: Ready")

        empty_mask = QImage()
        self.inpaint_mask = self.save_source_img(empty_mask)

        self.image_dict = {}
        self.image_index_dict = {}
        self.image_dict = {
            key: None
            for key in ["txt2img", "img2img", "inpaint", "upscale", "controlnet"]
        }
        self.image_index = None

        self.prompt_history = []
        self.neg_prompt_history = []
        self.displayed_image = None

        self.actionSettings.triggered.connect(self.settings_win.show)
        self.actionAbout.triggered.connect(app.aboutQt)
        self.actionExit.triggered.connect(self.close)
        self.generateButton.clicked.connect(self.launch_checks)
        self.nextImgButton.clicked.connect(lambda: self.cycle_images("next"))
        self.previousImgButton.clicked.connect(lambda: self.cycle_images("previous"))

        self.promptHistoryCombo.textActivated.connect(
            lambda: self.prompt_history_set(False)
        )
        self.negPromptHistoryCombo.textActivated.connect(
            lambda: self.prompt_history_set(True)
        )

        self.inpaintMaskEditorButton.clicked.connect(self.launch_inpaint)

        self.img2imgLoadButton.clicked.connect(
            lambda: self.image_select(self.img2imgLoadLine)
        )
        self.inpaintLoadButton.clicked.connect(
            lambda: self.image_select(self.inpaintLoadLine)
        )
        self.upscaleLoadButton.clicked.connect(
            lambda: self.image_select(self.upscaleLoadLine)
        )
        self.controlnetLoadButton.clicked.connect(
            lambda: self.image_select(self.controlnetLoadLine)
        )
        self.tabWidget.currentChanged.connect(self.set_tab_images)

        self.imageView.customContextMenuRequested.connect(self.image_view_menu)
        self.folder_date = self.get_date()
        self.add_controlnets()
        self.settings_win.show()
        print("--- App started")

    def add_controlnets(self):
        # Add controlnet models
        controlnet_models = sorted(
            [
                Path(controlnet_model).name
                for extension in ("*.safetensors", "*.ckpt")
                for controlnet_model in glob.glob(
                    f"{self.settings_win.comfyuiModelFolderValue.text()}/controlnet/{extension}"
                )
            ]
        )
        self.controlnetModelCombo.clear()
        self.controlnetModelCombo.addItems(controlnet_models)
        print("--- Added controlnet models:", controlnet_models)

    # Image view context menu
    def image_view_menu(self, position):
        if self.displayed_image:
            menu = QMenu()
            actions = ["Image to image", "Inpaint", "Upscale"]
            actions = [menu.addAction(action) for action in actions]
            action = menu.exec(self.imageView.mapToGlobal(position))
            source_image = self.displayed_image
            for i, act in enumerate(actions):
                if action == act:
                    self.tabWidget.setCurrentIndex(i + 1)
            self.gfxview_addimg(source_image)

    # Assign images to the appropriate tab
    def set_tab_images(self, current_tab_index=None):
        if not current_tab_index:
            current_tab_index = self.tabWidget.currentIndex()

        tab_images_keys = ["txt2img", "img2img", "inpaint", "upscale", "controlnet"]
        if current_tab_index in range(5):
            key = tab_images_keys[current_tab_index]
            if self.image_dict[key]:
                self.gfxview_addimg(
                    QImage.fromData(self.image_dict[key][self.image_index_dict[key]])
                )
                image_count = len(self.image_dict[key])
                imgDisplayIndex_text = (
                    image_count
                    if self.settings_win.keepImagesCheck.isChecked()
                    else self.image_index_dict[key] + 1
                )
                self.imgDisplayIndex.setText(
                    f"Image {imgDisplayIndex_text}/{image_count}"
                )

            elif self.displayed_image:
                self.imageView.clear()
                self.displayed_image = None
                self.imgDisplayIndex.setText("---")

    # Get data for chat log save
    def get_date(self):
        today = datetime.today()
        day = today.day
        month = today.month
        year = today.year
        return f"{day}-{month}-{year}"

    def get_file_path(self, title, filter):
        file_path = QFileDialog.getOpenFileName(self, title, "", filter)[0]
        return file_path

    # Browse for an image to load
    def image_select(self, line):
        image = self.get_file_path("Open file", "Images (*png)")
        if image:
            line.setText(image)
            pixmap = QImage(image)
            self.gfxview_addimg(pixmap)

    def get_comfyui_model_folder(self):
        comfyui_model_folder = Path(
            self.settings_win.comfyuiModelFolderValue.text()
        ).parent
        return comfyui_model_folder

    def launch_inpaint(self):
        if self.displayed_image:
            self.inpaint_mode = InpaintMaskEditor(
                self.displayed_image, self.inpaint_mask
            )
            self.inpaint_mode.show()

    def closeEvent(self, event):
        # close the child window when the parent window is closed
        self.settings_win.close()
        event.accept()

    def gfxview_addimg(self, pixmap):
        # create a pixmap item from the pixmap
        if pixmap:
            self.displayed_image = pixmap
            self.imageView.setPixmap(QPixmap(pixmap))
        else:
            self.imageView.clear()

    # Cycle through the images in the image list
    def cycle_images(self, mode):
        current_tab_index = self.tabWidget.currentIndex()
        tab_images_keys = ["txt2img", "img2img", "inpaint", "upscale", "controlnet"]
        if current_tab_index in [0, 1, 2, 3, 4]:
            key = tab_images_keys[current_tab_index]
            image_list = self.image_dict[key] if self.image_dict[key] else None

            if image_list:
                image_count = len(image_list)
                # Use a dictionary to map the mode to the increment or decrement of the image index
                delta = {"previous": -1, "next": 1}
                # Use a conditional expression to check if the mode is valid and update the image index accordingly
                self.image_index_dict[key] += (
                    delta[mode]
                    if mode in delta
                    and 0 <= self.image_index_dict[key] + delta[mode] < image_count
                    else 0
                )
                # Use a single line to create and set the pixmap from the image data
                self.gfxview_addimg(
                    QImage.fromData(image_list[self.image_index_dict[key]])
                )
                self.imgDisplayIndex.setText(
                    f"Image {self.image_index_dict[key]+1}/{image_count}"
                )

    # Get the prompt styles based on the style argument
    def prompt_styles(self, style):
        prompt_line = self.promptLine.toPlainText()

        with open(STYLES_FILE, "r") as stream:
            data = yaml.safe_load(stream)
            pos_prompt = str(data[style]["pos"])
            prompt_line_add = pos_prompt.replace("<prompt>", prompt_line)
            data[style]["pos"] = prompt_line_add
        return data[style]

    # Process the prompt and generate the image generation arguments
    def process_prompt(self):
        settings = self.settings_win

        if self.promptStyleCombo.currentIndex() != 0:
            style_dict = self.prompt_styles(
                self.promptStyleCombo.currentText().replace(": ", ":")
            )
            pos_prompt, neg_prompt = style_dict["pos"], style_dict["neg"]
        else:
            pos_prompt, neg_prompt = (
                self.promptLine.toPlainText(),
                self.negPromptLine.toPlainText(),
            )

        ckpt_name = settings.checkpointCombo.currentText()
        seed = (
            settings.seedValue.value() if settings.seedValue.value() != -1 else "random"
        )

        # Add base args
        img_gen_args = {
            "ckpt_name": ckpt_name,
            "pos_prompt": pos_prompt,
            "neg_prompt": neg_prompt,
            "batch_size": settings.batchValue.value(),
            "filename_prefix": f"SnugQt/{self.folder_date}/SnugQt",
            "seed": seed,
            "sampler_name": settings.samplerValue.currentText(),
            "scheduler": settings.schedulerValue.currentText(),
            "steps": settings.stepsValue.value(),
            "width": settings.imgWidthValue.value(),
            "height": settings.imgHeightValue.value(),
            "cfg": settings.cfgValue.value(),
            "iterations": settings.iterationsValue.value(),
            "clip_skip": settings.clipSkipValue.value(),
        }

        # Add optional args
        img_gen_args["external_vae"] = (
            settings.externalVaeCombo.currentText()
            if settings.useExternalVaeCheck.isChecked()
            else None
        )

        # LoRA
        img_gen_args["lora"] = (
            settings.loraCombo.currentText() if settings.loraCheck.isChecked() else None
        )
        img_gen_args["lora_strength"] = (
            settings.loraStrengthSpin.value()
            if settings.loraCheck.isChecked()
            else None
        )
        img_gen_args["lora_clip_strength"] = (
            settings.loraClipStrengthSpin.value()
            if img_gen_args["lora_strength"]
            else None
        )

        # Hires fix
        img_gen_args["hiresfix_scale_by"] = (
            self.hiresfixScaleByValue.value()
            if self.hiresFixCheck.isChecked()
            else None
        )
        img_gen_args["hiresfix_steps"] = (
            self.hiresfixStepsValue.value()
            if img_gen_args["hiresfix_scale_by"]
            else None
        )

        img_gen_args["hiresfix_denoise"] = (
            self.hiresfixDenoiseSpin.value()
            if img_gen_args["hiresfix_scale_by"]
            else None
        )

        # Upscale generated image
        img_gen_args["upscale_model"] = (
            settings.modelUpscaleCombo.currentText()
            if settings.modelUpscaleCheck.isChecked()
            else None
        )

        # img2img
        if self.tabWidget.currentIndex() == 1:
            img_gen_args["img2img_load"] = self.save_source_img(self.displayed_image)
            img_gen_args["img2img_denoise"] = self.img2imgDenoiseSpin.value()
        else:
            img_gen_args["img2img_load"] = None

        # inpainting
        if self.tabWidget.currentIndex() == 2:
            img_gen_args["inpainting_load"] = self.inpaint_mask
            img_gen_args["inpaint_denoise"] = self.inpaintDenoiseSpin.value()
            img_gen_args["outpaint_check"] = self.outpaintCheck.isChecked()
            # Outpainting
            if img_gen_args["outpaint_check"]:
                img_gen_args["outpaint_l"] = self.outpaintLSpin.value()
                img_gen_args["outpaint_r"] = self.outpaintRSpin.value()
                img_gen_args["outpaint_t"] = self.outpaintUSpin.value()
                img_gen_args["outpaint_b"] = self.outpaintDSpin.value()
                outpaint_img = self.displayed_image
                outpaint_img.save(str(Path(self.inpaint_mask)))
        else:
            img_gen_args["inpainting_load"] = None

        # Controlnet
        if self.tabWidget.currentIndex() == 4:
            img_gen_args["controlnet"] = self.controlnetLoadLine.text()
            img_gen_args["controlnet_strength"] = self.controlnetStrengthSpin.value()
            if self.controlnetScaleCheck.isChecked():
                img_gen_args["height"], img_gen_args["width"] = self.scale_to_image(
                    self.controlnetLoadLine.text()
                )
            img_gen_args["model"] = self.controlnetModelCombo.currentText()
        else:
            img_gen_args["controlnet"] = None

        # SDXL
        if settings.sdxlRefinerCheck.isChecked():
            img_gen_args["sdxl_refiner_ckpt"] = (
                settings.sdxlRefinerCheckpointCombo.currentText()
                if settings.sdxlRefinerCheck.isChecked()
                else None
            )
            img_gen_args["sdxl_refiner_steps"] = settings.sdxlRefinerStepsValue.text()
        else:
            img_gen_args["sdxl_refiner_ckpt"] = None

        return img_gen_args

    def scale_to_image(self, img_path):
        image = QImage(img_path)
        height, width = image.height(), image.width()
        new_height = height * self.controlnetScaleSpin.value()
        new_width = width * self.controlnetScaleSpin.value()

        def round_nearest(new_dimension):
            divisor = 8
            nearest = round(new_dimension / divisor) * divisor
            return nearest

        new_height = round_nearest(new_height)
        new_width = round_nearest(new_width)
        return new_height, new_width

    def add_prompt_history(self):
        self.prompt_history_add(
            self.promptLine.toPlainText(), False
        ) if self.promptLine.toPlainText() not in self.prompt_history else None
        self.prompt_history_add(
            self.negPromptLine.toPlainText(), True
        ) if self.negPromptLine.toPlainText() not in self.neg_prompt_history else None

    # Add the prompt input to the combo box and the history list
    def prompt_history_add(self, prompt_input, neg=False):
        combo = self.negPromptHistoryCombo if neg else self.promptHistoryCombo
        history = self.neg_prompt_history if neg else self.prompt_history
        combo.addItem(str(prompt_input[:96]))
        history.append(prompt_input)

    # Set the prompt input field to the saved history
    def prompt_history_set(self, neg=False):
        combo = self.negPromptHistoryCombo if neg else self.promptHistoryCombo
        line = self.negPromptLine if neg else self.promptLine
        history = self.neg_prompt_history if neg else self.prompt_history
        if combo.count() >= 1:
            text = history[int(combo.currentIndex())]
            line.setPlainText(text)

    def save_source_img(self, source):
        # Create a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            # Open an image file
            source_image = QImage(source)
            # Save the image to the temporary file
            source_image.save(tmp.name, format="PNG")
            # Get the path of the temporary file
            source_image_path = tmp.name
            # print(f"The path of the temporary PNG file is: {source_image_path}")
        return source_image_path

    # Check for any failures before launch
    def launch_checks(self):
        standalone = None
        if not self.displayed_image and self.tabWidget.currentIndex() > 0:
            print("--- No image selected")
            return
        if self.tabWidget.currentIndex() == 3:
            if not self.settings_win.modelUpscaleCombo.currentText():
                print("--- No upscale model selected")
                return
            else:
                standalone = "upscale"
        self.launch_thread(standalone)

    # Start a thread to load the model asynchronously
    def launch_thread(self, standalone):
        # Determine SD or standalone mode
        img_gen_args = {}
        if not standalone:
            img_gen_args = self.process_prompt()
            img_gen_args["so_upscale_model"] = None
        elif standalone == "upscale":
            img_gen_args[
                "so_upscale_model"
            ] = self.settings_win.modelUpscaleCombo.currentText()
            img_gen_args["so_upscale_image"] = self.save_source_img(
                self.displayed_image
            )
            img_gen_args["downscale"] = (
                self.upscaleSpin.value() / 100
                if self.upscaleDownscaleCheck.isChecked()
                else None
            )

        self.add_prompt_history()
        self.statusbar.showMessage("Status: Generating...")
        self.generateButton.setEnabled(False)
        self.RunAPI_Thread = RunAPI(
            img_gen_args,
            self.tabWidget.currentIndex(),
        )
        self.RunAPI_Thread.final_resultReady.connect(self.RunAPI_handleResult)
        self.RunAPI_Thread.finished.connect(self.RunAPI_Thread.deleteLater)
        self.RunAPI_Thread.start()

    def completion_imgs_tabs(self, temp_image_list, tab_index):
        tab_images_keys = ["txt2img", "img2img", "inpaint", "upscale", "controlnet"]
        if tab_index in range(5):
            key = tab_images_keys[tab_index]

            if self.settings_win.keepImagesCheck.isChecked():
                if not self.image_dict[key]:
                    self.image_dict[key] = []
                for image in temp_image_list:
                    if (
                        len(self.image_dict[key])
                        >= self.settings_win.maxImagesSpin.value()
                    ):
                        self.image_dict[key].pop(0)
                    self.image_dict[key].append(image)
                self.image_index_dict[key] = len(self.image_dict[key]) - 1
            else:
                self.image_dict[key] = temp_image_list
                self.image_index_dict[key] = 0

    # Handle result of the image generation from API
    @Slot(list, bool, int)
    def RunAPI_handleResult(self, temp_image_list, success, tab_index):
        if success:
            self.completion_imgs_tabs(temp_image_list, tab_index)
            self.set_tab_images(tab_index)

        self.on_completion(success)

    # Final handle of result
    def on_completion(self, success):
        if success:
            self.statusbar.showMessage("Success: Generation complete")
        else:
            self.statusbar.showMessage("Error: Generation failed")
        self.generateButton.setEnabled(True)
        app.alert(self.centralwidget)


if __name__ == "__main__":
    # Create a Qt application instance
    app = QApplication(sys.argv)
    extra = {"pyside6": True, "density_scale": "-1", "font_family": ""}
    apply_stylesheet(
        app, theme="dark_lightgreen.xml", css_file="assets/dark_theme.css", extra=extra
    )
    if platform.system() == "Windows":
        app.setStyle("Fusion")

    # Create a chat window instance and show it
    window = MagiApp()
    window.show()

    # Start the Qt event loop
    app.exec()
