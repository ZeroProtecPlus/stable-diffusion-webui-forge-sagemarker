import os
import subprocess
from contextlib import suppress

os.chdir("stable-diffusion-webui-forge-sagemarker/extensions")  


def download_ext(command):
    print("Downloading Extensions")
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Extension downloaded successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: Extension download failed with the following output:\n{e.stderr.decode('utf-8')}")

extensions = [
    'git clone https://github.com/w-e-w/sd-fast-pnginfo.git',
    'git clone https://github.com/etherealxx/batchlinks-webui.git',
    'git clone https://github.com/Bing-su/adetailer.git',
    'git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete.git',
    'git clone https://github.com/BlafKing/sd-civitai-browser-plus.git',
    'git clone https://github.com/zanllp/sd-webui-infinite-image-browsing.git',
    'git clone https://github.com/Coyote-A/ultimate-upscale-for-automatic1111.git',
    'git clone https://github.com/uwidev/sd_extension-prompt_formatter',
    'git clone https://github.com/picobyte/stable-diffusion-webui-wd14-tagger',
    'git clone https://github.com/mcmonkeyprojects/sd-dynamic-thresholding',
    'git clone https://github.com/huchenlei/sd-webui-openpose-editor',
    'git clone https://github.com/Mikubill/sd-webui-controlnet',
    'git clone https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111',
    'git clone https://github.com/hako-mikan/sd-webui-regional-prompter',
    'git clone https://github.com/catppuccin/stable-diffusion-webui',
    'git clone https://github.com/thomasasfk/sd-webui-aspect-ratio-helper'
]

for extension in extensions:
    download_ext(extension)