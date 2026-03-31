import os
import subprocess
import platform

def start_file(file_path):
    if platform.system() == "Windows":
        os.startfile(file_path)
    elif platform.system() == "Darwin":
        subprocess.call(["open", file_path])
    else:
        subprocess.call(["xdg-open", file_path])
