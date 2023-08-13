import glob
import platform
import random
import sys
from pathlib import Path

import yaml
from PySide6 import QtWidgets
from PySide6.QtCore import QSize, QThread, Signal, Slot
from PySide6.QtGui import QIcon, QImage, QPixmap
from PySide6.QtWidgets import QApplication, QFileDialog, QGraphicsPixmapItem, QGraphicsScene
from qt_material import apply_stylesheet

from comfy_api_fetch import ws_generate
from inpaint_window import InpaintMaskEditor
from main_window import Ui_MainWindow
from settings_window import Ui_SettingsDialog

SETTINGS_FILE = Path("settings.yaml")
APP_ICON = Path("assets/appicon.png")


class RunAPI(QThread):
    final_resultReady = Signal(list, bool)

    def __init__(self, img_gen_args: dict):
        super().__init__()
        self.img_gen_args = img_gen_args
        # print("Img gen args:", self.img_gen_args)

    # Launch img_gen
    def run(self):
        if self.img_gen_args:
            try:
                self.img_gen()
            except Exception as error:
                self.final_resultReady.emit(None, False)
                print("--- Error during generation:\n", error)
                return
            
    # Generate the image and emit the final result
    def img_gen(self):
        img_fetch = ws_generate()
        image_list = []

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
            image_list.extend(generate_image_list(images))
            # Increment the seed if random_seed is False
            if not random_seed:
                self.img_gen_args["seed"] += 1

        # Check if no images were generated
        if not image_list:
            print("No images were generated")
            self.final_resultReady.emit(None, False)

        self.final_resultReady.emit(image_list, True)


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
        self.img2imgLoadButton.clicked.connect(self.img2img_load_images)

        self.saveSettingsButton.clicked.connect(self.save_settings)
        self.reloadModelsButton.clicked.connect(self.add_models)
        self.inpaintMaskEditorButton.clicked.connect(self.inpaint)

        self.load_settings()
        self.comfyui_folder = Path(self.comfyuiModelFolderValue.text()).parent
        self.img2img_load_images()

    def inpaint(self):
        if self.img2imgLoadCombo.currentText():
            img_input_path = Path(f"{self.comfyui_folder}/input/{self.img2imgLoadCombo.currentText()}")
            img_mask_path = Path(f"{self.comfyui_folder}/input/snugqt_mask.png")
            if QImage(img_input_path).height() > 0:
                self.inpaint_mode = InpaintMaskEditor(str(img_input_path), img_mask_path)
                self.inpaint_mode.show()
            else:
                print('--- Error: Invalid image')
        else:
            print('--- Error: Invalid image')

    def get_directory_path(self, title):
        directory_path = str(QFileDialog.getExistingDirectory(self, title))
        return directory_path

    def load_settings(self):
        with open(SETTINGS_FILE, "r") as stream:
            data = yaml.safe_load(stream)

            # Checkpoints
            checkpoints = data["checkpoints"]
            self.comfyuiModelFolderValue.setText(checkpoints["comfy_model_folder"])
            self.comfyuiExtraFolderValue.setText(checkpoints["comfy_extra_model_folder"])
            self.add_models()
            self.sd12CheckpointCombo.setCurrentText(checkpoints["sd12"])
            self.sdxlBaseCheckpointCombo.setCurrentText(checkpoints["sdxl_base"])
            self.sdxlRefinerCheckpointCombo.setCurrentText(checkpoints["sdxl_refiner"])
            self.sd12VaeCombo.setCurrentText(checkpoints["sd12_vae"])
            self.sdxlVaeCombo.setCurrentText(checkpoints["sdxl_vae"])
            self.modelUpscaleCombo.setCurrentText(checkpoints["upscale_model"])
            self.useExternalVaeCheck.setChecked(checkpoints["use_ex_vae"])
            # Parameters
            params = data["parameters"]
            self.modeSelectCombo.setCurrentText(params["mode"])
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
            self.hiresFixCheck.setChecked(params["hrf_check"])
            self.hiresfixScaleByValue.setValue(params["hrf_scaleby"])
            self.hiresfixStepsValue.setValue(params["hrf_steps"])
            # Lora
            lora = data["lora"]
            self.loraCheck.setChecked(lora["use"])
            self.sd12LoraCombo.setCurrentText(lora["sd12"])
            self.sdxlLoraCombo.setCurrentText(lora["sdxl"])
            self.loraStrengthSpin.setValue(lora["model_strength"])
            self.loraClipStrengthSpin.setValue(lora["clip_strength"])

    # Save settings to settings.yaml
    def save_settings(self):
        with open(SETTINGS_FILE, "r") as stream:
            data = yaml.safe_load(stream)

            # Checkpoints
            data["checkpoints"].update({
                "comfy_model_folder": self.comfyuiModelFolderValue.text(),
                "comfy_extra_model_folder": self.comfyuiExtraFolderValue.text(),
                "sd12": self.sd12CheckpointCombo.currentText(),
                "sdxl_base": self.sdxlBaseCheckpointCombo.currentText(),
                "sdxl_refiner": self.sdxlRefinerCheckpointCombo.currentText(),
                "sd12_vae": self.sd12VaeCombo.currentText(),
                "sdxl_vae": self.sdxlVaeCombo.currentText(),
                "use_ex_vae": self.useExternalVaeCheck.isChecked(),
                "upscale_model": self.modelUpscaleCombo.currentText()
            })
            # Parameters
            data["parameters"].update({
                "mode": self.modeSelectCombo.currentText(),
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
                "hrf_check": self.hiresFixCheck.isChecked(),
                "hrf_scaleby": self.hiresfixScaleByValue.value(),
                "hrf_steps": self.hiresfixStepsValue.value(),
            })
            # Lora
            data["lora"].update({
                "use": self.loraCheck.isChecked(),
                "sd12": self.sd12LoraCombo.currentText(),
                "sdxl": self.sdxlLoraCombo.currentText(),
                "model_strength": self.loraStrengthSpin.value(),
                "clip_strength": self.loraClipStrengthSpin.value(),
            })

        with open(SETTINGS_FILE, "w") as stream:
            yaml.dump(data, stream, default_flow_style=False)
        print("Settings saved")

    # Add the model names to the combo boxes
    def add_models(self):
        # Add ckpts
        ckpts = sorted([Path(ckpt).name for extension in ("*.safetensors", "*.ckpt") for ckpt in glob.glob(f"{self.comfyuiModelFolderValue.text()}/checkpoints/{extension}")])
        extra_ckpts = sorted([Path(extra_ckpt).name for extension in ("*.safetensors", "*.ckpt") for extra_ckpt in glob.glob(f"{self.comfyuiExtraFolderValue.text()}/{extension}")])
        for combo in (self.sd12CheckpointCombo, self.sdxlBaseCheckpointCombo, self.sdxlRefinerCheckpointCombo):
            combo.clear()
            combo.addItems(ckpts)
            combo.addItems(extra_ckpts)
        print('--- Added checkpoints:', ckpts, extra_ckpts)

        # Add VAEs
        vaes = sorted([Path(vae).name for extension in ("*.safetensors", "*.ckpt") for vae in glob.glob(f"{self.comfyuiModelFolderValue.text()}/vae/{extension}")])
        for combo in (self.sd12VaeCombo, self.sdxlVaeCombo):
            combo.clear()
            combo.addItems(vaes)
        print('--- Added VAEs:', vaes)

        # Add LoRAs
        loras = sorted([Path(lora).name for extension in ("*.safetensors", "*.ckpt") for lora in glob.glob(f"{self.comfyuiModelFolderValue.text()}/loras/{extension}")])
        for combo in (self.sd12LoraCombo, self.sdxlLoraCombo):
            combo.clear()
            combo.addItems(loras)
        print('--- Added LoRAs:', loras)

        # Add upscale models
        upscale_models = sorted([Path(upscale_model).name for extension in ("*.pth", "*.onxx")for upscale_model in glob.glob(f"{self.comfyuiModelFolderValue.text()}/upscale_models/{extension}")])
        self.modelUpscaleCombo.clear()
        self.modelUpscaleCombo.addItems(upscale_models)
        print('--- Added upscale models:', upscale_models)

    # Browse for ComfyUI model folder
    def comfyui_model_folder_select(self):
        model_folder = self.get_directory_path("Select ComfyUI model directory")
        if model_folder:
            self.comfyuiModelFolderValue.setText(model_folder)
            self.add_models()

    # Browse for ComfyUI extra models folder
    def comfyui_extra_folder_select(self):
        extra_model_folder = self.get_directory_path("Select ComfyUI extra checkpoint directory")
        if extra_model_folder:
            self.comfyuiExtraFolderValue.setText(extra_model_folder)
            self.add_models()
    
    def img2img_load_images(self):
        img2img_images = sorted([Path(img2img_image).name for extension in ("*.png", "*.jpg", "*.jpeg")for img2img_image in glob.glob(f"{self.comfyui_folder}/input/{extension}")])
        self.img2imgLoadCombo.clear()
        self.img2imgLoadCombo.addItems(img2img_images)

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

        self.image_list = []
        self.prompt_history = []
        self.neg_prompt_history = []

        self.actionSettings.triggered.connect(self.settings_win.show)
        self.actionExit.triggered.connect(self.close)
        self.generateButton.clicked.connect(self.launch_thread)
        self.nextImgButton.clicked.connect(lambda: self.cycle_images("next"))
        self.previousImgButton.clicked.connect(lambda: self.cycle_images("previous"))

        self.promptHistoryCombo.textActivated.connect(self.prompt_history_set)
        self.negPromptHistoryCombo.textActivated.connect(self.neg_prompt_history_set)
        print('--- App started')
        self.settings_win.show()

    def closeEvent(self, event):
        # close the child window when the parent window is closed
        self.settings_win.close()
        event.accept()

    def gfxview_addimg(self, pixmap):
        # create a pixmap item from the pixmap
        self.scene = QGraphicsScene()
        self.pixmap_item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.pixmap_item)
        self.imgLabel.setScene(self.scene)

    # Cycle through the images in the image list
    def cycle_images(self, mode):
        image_count = len(self.image_list)

        if self.image_list:
            # Use a dictionary to map the mode to the increment or decrement of the image index
            delta = {"previous": -1, "next": 1}
            # Use a conditional expression to check if the mode is valid and update the image index accordingly
            self.image_index += delta[mode] if mode in delta and 0 <= self.image_index + delta[mode] < image_count else 0
            # Use a single line to create and set the pixmap from the image data
            self.gfxview_addimg(QPixmap.fromImage(QImage.fromData(self.image_list[self.image_index])))
            image_display_index = self.image_index + 1
            self.imgDisplayIndex.setText(f"Image {image_display_index}/{image_count}")

    # Process the prompt and generate the image generation arguments
    def process_prompt(self):
        # Use a dictionary to map the mode to the corresponding checkpoint and vae combo boxes
        mode_combo = {
            "Stable Diffusion 1/2": (self.settings_win.sd12CheckpointCombo, self.settings_win.sd12VaeCombo, self.settings_win.sd12LoraCombo),
            "SDXL": (self.settings_win.sdxlBaseCheckpointCombo, self.settings_win.sdxlVaeCombo, self.settings_win.sdxlLoraCombo)
        }
        ckpt_name = mode_combo[self.settings_win.modeSelectCombo.currentText()][0].currentText()
        external_vae = mode_combo[self.settings_win.modeSelectCombo.currentText()][1].currentText() if self.settings_win.useExternalVaeCheck.isChecked() else None
        lora = mode_combo[self.settings_win.modeSelectCombo.currentText()][2].currentText() if self.settings_win.loraCheck.isChecked() else None

        # Get the seed value from the settings window or generate a random one using a conditional expression
        seed = self.settings_win.seedValue.value() if self.settings_win.seedValue.value() != -1 else "random"

        # Create a dictionary of image generation arguments with the values from the prompt and settings window using f-strings and str() where needed
        settings=self.settings_win
        img_gen_args = {
            "ckpt_name": ckpt_name,
            "hiresfix_scale_by": settings.hiresfixScaleByValue.value() if settings.hiresFixCheck.isChecked() else None,
            "hiresfix_steps": settings.hiresfixStepsValue.value() if settings.hiresFixCheck.isChecked() else None,
            "external_vae": external_vae,
            "lora": lora,
            "pos_prompt": self.promptLine.toPlainText(),
            "neg_prompt": self.negPromptLine.toPlainText(),
            "batch_size": settings.batchValue.value(),
            "filename_prefix": "SnugQt/SnugQt",
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

        comfyui_path = Path(settings.comfyuiModelFolderValue.text()).parent
        mask_path = Path(f"{comfyui_path}/input/snugqt_mask.png")

        img_gen_args["lora_strength"] = settings.loraStrengthSpin.value() if settings.loraCheck.isChecked() else None
        img_gen_args["lora_clip_strength"] = settings.loraClipStrengthSpin.value() if img_gen_args["lora_strength"] else None
        img_gen_args["upscale_model"] = settings.modelUpscaleCombo.currentText() if settings.modelUpscaleCheck.isChecked() else None
        
        img_gen_args["img2img_load"] = settings.img2imgLoadCombo.currentText() if settings.img2imgInpaintingCheck.isChecked() and settings.img2imgRadio.isChecked() else None
        img_gen_args["inpainting_load"] = mask_path if settings.img2imgInpaintingCheck.isChecked() and settings.inpaintingRadio.isChecked() else None
        img_gen_args["img2img_denoise"] = settings.img2imgDenoiseSpin.value() if img_gen_args["img2img_load"] or img_gen_args["inpainting_load"] else None
        
        if settings.modeSelectCombo.currentText() == "SDXL":
            img_gen_args["sdxl_refiner_ckpt"] = settings.sdxlRefinerCheckpointCombo.currentText() if settings.sdxlRefinerCheck.isChecked() else None
            img_gen_args["sdxl_refiner_steps"] = settings.sdxlRefinerStepsValue.text()
        else:
            img_gen_args["sdxl_refiner_ckpt"] = None

        return img_gen_args
    
    # Start a thread to load the model asynchronously
    def launch_thread(self):
        img_gen_args = self.process_prompt()
        self.statusbar.showMessage("Status: Generating...")
        self.generateButton.setEnabled(False)
        self.RunAPI_Thread = RunAPI(img_gen_args)
        self.RunAPI_Thread.final_resultReady.connect(self.RunAPI_handleResult)
        self.RunAPI_Thread.finished.connect(self.RunAPI_Thread.deleteLater)
        self.add_prompt_history()

    # Add prompt history to combo box
    def add_prompt_history(self):
        self.prompt_history_add(
            self.promptLine.toPlainText()
        ) if self.promptLine.toPlainText() not in self.prompt_history else None
        self.neg_prompt_history_add(
            self.negPromptLine.toPlainText()
        ) if self.negPromptLine.toPlainText() not in self.neg_prompt_history else None

        self.RunAPI_Thread.start()
        
    # Handle result of the image generation from API
    @Slot(list, bool)
    def RunAPI_handleResult(self, image_list, success):
        if success is False:
            self.on_completion(success)
            return
        self.image_list = image_list
        self.image_index = 0
        self.gfxview_addimg(QPixmap.fromImage(QImage.fromData(self.image_list[0])))
        self.imgDisplayIndex.setText(f"Image 1/{len(self.image_list)}")
        self.on_completion(success)

    # Final handle of result
    def on_completion(self, success):
        if success:
            self.statusbar.showMessage("Status: Generation complete")
        else:
            self.statusbar.showMessage("Error: Generation failed")
        self.generateButton.setEnabled(True)
        app.alert(self.centralwidget)

    # Add the prompt input to the combo box and the history list
    def prompt_history_add(self, prompt_input):
        self.promptHistoryCombo.addItem(str(prompt_input[:96]))
        self.prompt_history.append(prompt_input)

    # Add the negative prompt input to the combo box and the history list
    def neg_prompt_history_add(self, neg_prompt_input):
        self.negPromptHistoryCombo.addItem(str(neg_prompt_input[:96]))
        self.neg_prompt_history.append(neg_prompt_input)

    # Set the prompt input field to the saved history
    def prompt_history_set(self):
        if self.promptHistoryCombo.count() >= 1:
            text = self.prompt_history[int(self.promptHistoryCombo.currentIndex())]
            self.promptLine.setPlainText(text)

    # Set the negative prompt input field to the saved history
    def neg_prompt_history_set(self):
        if self.negPromptHistoryCombo.count() >= 1:
            text = self.neg_prompt_history[
                int(self.negPromptHistoryCombo.currentIndex())
            ]
            self.negPromptLine.setPlainText(text)


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

# pyside6-uic .\assets\ui\main_window.ui -o .\main_window.py; pyside6-uic .\assets\ui\settings_window.ui -o .\settings_window.py