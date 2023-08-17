# SnugQt
A Qt frontend for image generation that uses ComfyUI

Supports Windows, Linux and Mac(?)

**Features:**
- Supports SD 1.x, SD 2.x, SDXL, SDXL Refiner
- txt2img, img2img, hires fix
- Inpainting
- Loras
- Upscaling

**Installation:**

First make sure Python (3.10+ recommended) and GIT are installed. Then:
```
git clone https://github.com/shinomakoi/SnugQt
cd SnugQt
```
Optionally create a virtual environment (recommended)

```
python -m venv .venv
source ./.venv/bin/activate ### For Linux
.\.venv\Scripts\activate ## For Windows
```
```
pip install -r requirements.txt
```
You can update to latest version with: `git pull`

**Usage:**

Make sure you have launched ComfyUI first, then to launch SnugQt run: 
```
python main.py
```
You can change settings in File > Settings. Make sure to set the path to the 'ComfyUI/models' folder (click the ... button to select).
Images are saved in the ComfyUI/ouput/SnugQT folder.

![image](https://github.com/shinomakoi/SnugQt/assets/112139428/7474dcb8-a37e-4fa9-b1a9-2819663a9e4e)
