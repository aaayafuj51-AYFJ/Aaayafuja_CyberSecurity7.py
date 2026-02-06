import os
import subprocess
import platform

def run_external_batch(file_path):
    """Safely executes a .bat or .sh file depending on the platform."""
    if not os.path.exists(file_path):
        return False, "File not found."
    
    try:
        if platform.system() == "Windows":
            result = subprocess.run([file_path], capture_output=True, text=True, shell=True)
        else:
            # On Unix, ensure it's executable
            os.chmod(file_path, 0o755)
            result = subprocess.run([file_path], capture_output=True, text=True)
            
        return True, result.stdout
    except Exception as e:
        return False, str(e)

def list_workspace_files(directory="."):
    """Lists files in the current workspace for the GUI."""
    try:
        return os.listdir(directory)
    except Exception:
        return []
