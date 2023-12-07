import subprocess
import sys

if sys.platform.startswith('win'):
    # Path to your python script
    path = r'YOUR PATH TO PYTHON FILE'

    # Run Python Script with out terminal
    subprocess.Popen(['pythonw.exe', path], creationflags=subprocess.CREATE_NO_WINDOW) # CREATE_NO_WINDOW using only for windows
else:
    print('This Example only for windows')