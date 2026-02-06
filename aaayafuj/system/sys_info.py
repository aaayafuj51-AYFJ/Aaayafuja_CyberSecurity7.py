import platform
import os

def get_platform_data():
    return {
        "os": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "arch": platform.machine(),
        "processor": platform.processor(),
        "user": os.getlogin() if hasattr(os, 'getlogin') else "unknown"
    }
