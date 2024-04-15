import os
    
def enable_zrok(token):
    os.system(f"zrok enable {token}")
    
def connection():
    try:
        os.system("zrok share public http://localhost:7860 --headless")
    except Exception as e:
        print(f"Error al conectarse, verifique su token.\n {e}")