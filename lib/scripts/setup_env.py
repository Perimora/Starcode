import os
import sys
import subprocess

from IPython.display import clear_output

VENV_PATH= ".venv"

def create_venv():
    """
    Check if a virtual environment exists at the given path.
    If not, create a new one.
    """

    # check if the virtual environment exists
    if os.path.exists(VENV_PATH):
        print(f"Virtual environment already exists at {VENV_PATH}.")
    else:
        print(f"No virtual environment found at {VENV_PATH}. Creating one...")
        try:
            # create a virtual environment
            subprocess.run([sys.executable, "-m", "venv", VENV_PATH], check=True)
            print(f"Virtual environment created at {VENV_PATH}.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to create virtual environment: {e}")
            sys.exit(1)

def install_requirements():
    """
    Installs all dependencies specified in 'requirements.txt in repository root.'
    """
    
    try:
        result = subprocess.run(
            ["pip", "install", "-r", "requirements.txt"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            clear_output()
            print("Einrichtung erfolgreich!")
        else:
            print("Fehler bei der Installation:")
            print(result.stderr)
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

