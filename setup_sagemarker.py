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

for command, message in commands:
    run_command(command, message)