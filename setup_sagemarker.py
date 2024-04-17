import os
import subprocess
from contextlib import suppress

os.chdir("/home/studio-lab-user")  

def run_command(command, message):
    print(f"Please wait, {message} is loading...")
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{message} completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {message} failed with the following output:\n{e.stderr.decode('utf-8')}")

commands = [
    ('conda install conda -y', 'Conda'),
    ('conda update -n base conda -y', 'Update'),
    ('conda install -n base python=3.10 -y', 'Python'),
    ('conda install -q -y glib=2.51.0', 'glib')
]

def download_ext(command):
    print("Downloading Extensions")
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Extension downloaded successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: Extension download failed with the following output:\n{e.stderr.decode('utf-8')}")

extensions = [
    'git clone https://github.com/NoCrypt/sd-fast-pnginfo.git',
    'git clone https://github.com/etherealxx/batchlinks-webui.git',
    'git clone https://github.com/Bing-su/adetailer.git',
    'git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete.git',
    'git clone https://github.com/BlafKing/sd-civitai-browser-plus.git',
    'git clone https://github.com/zanllp/sd-webui-infinite-image-browsing.git',
    'git clone https://github.com/Coyote-A/ultimate-upscale-for-automatic1111.git'
]

for command, message in commands:
    run_command(command, message)

os.chdir('~/stable-diffusion-webui-forge-sagemarker/extensions')  

for extension in extensions:
    download_ext(extension)