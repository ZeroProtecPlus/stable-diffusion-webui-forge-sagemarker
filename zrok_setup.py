import os

def installation():
    os.system("mkdir .temp")
    os. chdir(".temp")

    os.system("wget https://github.com/openziti/zrok/releases/download/v0.4.23/zrok_0.4.23_linux_amd64.tar.gz")
    os.system("mkdir /.temp/zrok")

    os.system("tar -xf ./zrok*linux*.tar.gz -C /.temp/zrok")
    os.system("mkdir -p /.temp/zrok/bin && install /.temp/zrok/zrok /.temp/zrok/bin")


    os.environ['PATH'] = "/.temp/zrok/bin:" + os.environ['PATH']
    os.system("zrok version")
    
if not os.path.exists("/home/studio-lab-user/.temp"):
    installation()
else:
    print("Zrok is already installed")