import subprocess
import sys
import os

def launch_gui():
    script_path = os.path.join(os.path.dirname(__file__), "judy_gui.py")
    subprocess.Popen([sys.executable, script_path], shell=True)

if __name__ == "__main__":
    launch_gui()