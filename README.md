# SnugQt
A Qt frontend for image generation that uses ComfyUI

Supports Windows, Linux and Mac(?)

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

**Usage:**

Make sure you have launched ComfyUI first, then to launch SnugQt run: 
```
python main.py
```
You can set the settings in File > Settings. Make sure to set the paths to the checkpoint/VAE folders (click the .. button to select them) - these must be recognised by ComfyUI.
Images are saved in the ComfyUI/ouput/SnugQT folder.

![image](https://github.com/shinomakoi/SnugQt/assets/112139428/23238904-323c-4f95-bbf8-32469d65f052)
