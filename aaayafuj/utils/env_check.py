import sys
import os
import platform

def run_diagnostic():
    print("="*60)
    print(" AAAYAFUJ ENVIRONMENT DIAGNOSTIC TOOL ")
    print("="*60)
    
    print(f"OS Platform:    {platform.platform()}")
    print(f"Python Version: {sys.version}")
    print(f"Python Exec:    {sys.executable}")
    
    # Path Analysis
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    print(f"Project Root:   {project_root}")
    
    print("\n--- Checking Path Health ---")
    if os.name == 'nt':
        python_dir = os.path.dirname(sys.executable)
        scripts_dir = os.path.join(python_dir, "Scripts")
        
        if not os.path.exists(scripts_dir):
            print("[!] Warning: Scripts directory not found. Pip might be broken.")
        else:
            print("[+] Scripts directory found.")
            
    print("\n--- Troubleshooting 'Fatal Error in Launcher' ---")
    print("If you see this error, it means 'pip.exe' cannot find your 'python.exe'.")
    print("\n[SOLUTION]")
    print(f"1. Open your terminal (CMD or PowerShell)")
    print(f"2. Type: {sys.executable} -m pip install --upgrade pip")
    print(f"3. Type: {sys.executable} -m pip install -r requirements.txt")
    
    print("\n--- Checking Package Loadability ---")
    try:
        import aaayafuj
        print("[+] Aaayafuj package is loadable.")
    except ImportError:
        print("[-] Aaayafuj package is NOT in your PYTHONPATH.")
        print(f"    Try running: set PYTHONPATH=%PYTHONPATH%;{project_root}")

    print("="*60)

if __name__ == "__main__":
    run_diagnostic()
