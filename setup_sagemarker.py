import os
import time
token = ""

def enable_zrok(token):
    os.system(f"zrok enable {token}")
    
def connection():
    time.sleep(15)
    try:
        os.system("zrok share public http://localhost:7860 --headless")
    except Exception as e:
        print(f"Error al conectarse, verifique su token.\n {e}")

try:
    enable_zrok(token)
except Exception as e:
    print(f"ERROR - {e}")
    
connection()