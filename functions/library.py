import subprocess
import sys
from functions.loading import loading_animation

def library_check():
    print("Verificando bibliotecas necessárias...")
    loading_animation()

    try:
        import Pillow
    except ImportError:
        
        subprocess.run([sys.executable, "-m", "pip", "install", "Pillow"], check=True)