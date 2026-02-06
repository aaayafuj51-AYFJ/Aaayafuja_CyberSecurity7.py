import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import subprocess
import threading
import os
import sys
import platform

# Ensure project root is in path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from aaayafuj.version import __version__
    from aaayafuj.utils.formatter import RED, GREEN, RESET
except ImportError:
    __version__ = "7.0.4-LTS-NET"

class AaayafujNetGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(f"Aaayafuj Net - Desktop Command Center v{__version__}")
        self.root.geometry("1100x700")
        self.root.configure(bg="#0a0a0c")
        
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.setup_styles()
        
        # UI State
        self.current_process = None
        self.is_running = False
        
        self.create_widgets()
        self.log("[*] Aaayafuj Net Environment Initialized.")
        self.log(f"[*] OS: {platform.system()} {platform.release()}")
        self.log(f"[*] Python: {sys.version.split()[0]}")

    def setup_styles(self):
        self.style.configure("TFrame", background="#0a0a0c")
        self.style.configure("Sidebar.TFrame", background="#121218")
        self.style.configure("TLabel", background="#0a0a0c", foreground="#e2e8f0", font=("Fira Code", 10))
        self.style.configure("Header.TLabel", font=("Fira Code", 14, "bold"), foreground="#ef4444")
        self.style.configure("Action.TButton", font=("Fira Code", 10, "bold"), padding=10)
        
    def create_widgets(self):
        # Main Container
        self.main_container = ttk.Frame(self.root)
        self.main_container.pack(fill=tk.BOTH, expand=True)

        # Sidebar
        self.sidebar = ttk.Frame(self.main_container, style="Sidebar.TFrame", width=250)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.pack_propagate(False)

        ttk.Label(self.sidebar, text="AAAYAFUJ NET", style="Header.TLabel", background="#121218").pack(pady=20, padx=10)
        
        # Category Buttons
        categories = [
            ("🏠 Dashboard", self.show_dashboard),
            ("🔍 Security Scan", lambda: self.set_cmd("scan all")),
            ("🌐 Network Hub", lambda: self.set_cmd("net info")),
            ("💻 System Audit", lambda: self.set_cmd("sys info")),
            ("📦 Asset Manager", lambda: self.set_cmd("assets list")),
            ("🛡️ Compliance", lambda: self.set_cmd("sec status")),
            ("🤖 AI Assistant", lambda: self.set_cmd("bot")),
            ("📜 Log Viewer", lambda: self.set_cmd("logs list")),
        ]

        for text, cmd in categories:
            btn = tk.Button(self.sidebar, text=text, bg="#1a1a24", fg="#e2e8f0", 
                            activebackground="#ef4444", activeforeground="white",
                            font=("Fira Code", 10), bd=0, pady=12, anchor="w", padx=20,
                            command=cmd)
            btn.pack(fill=tk.X, pady=2)

        # Batch runner section
        ttk.Separator(self.sidebar, orient='horizontal').pack(fill=tk.X, pady=20, padx=10)
        tk.Button(self.sidebar, text="⚡ Run .bat File", bg="#991b1b", fg="white",
                  font=("Fira Code", 10, "bold"), bd=0, pady=12, command=self.run_batch_file).pack(fill=tk.X, padx=10)

        # Workspace
        self.workspace = ttk.Frame(self.main_container)
        self.workspace.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Top Bar (Command Input)
        self.top_bar = ttk.Frame(self.workspace)
        self.top_bar.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(self.top_bar, text="CMD >").pack(side=tk.LEFT, padx=(0, 10))
        self.cmd_entry = tk.Entry(self.top_bar, bg="#121218", fg="#ef4444", 
                                  insertbackground="white", font=("Fira Code", 11), 
                                  bd=1, relief=tk.FLAT)
        self.cmd_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.cmd_entry.bind("<Return>", lambda e: self.execute_command())

        self.run_btn = tk.Button(self.top_bar, text="EXECUTE", bg="#ef4444", fg="white",
                                 font=("Fira Code", 9, "bold"), padx=15, command=self.execute_command)
        self.run_btn.pack(side=tk.LEFT, padx=5)

        # Terminal Output
        self.terminal = scrolledtext.ScrolledText(self.workspace, bg="#050507", fg="#00ff41",
                                                font=("Consolas", 11), insertbackground="white",
                                                selectbackground="#ef4444", bd=0)
        self.terminal.pack(fill=tk.BOTH, expand=True)
        
        # Status Bar
        self.status_bar = ttk.Frame(self.workspace)
        self.status_bar.pack(fill=tk.X, pady=(10, 0))
        self.status_label = ttk.Label(self.status_bar, text="READY", foreground="#666")
        self.status_label.pack(side=tk.LEFT)

    def log(self, text):
        self.terminal.insert(tk.END, text + "\n")
        self.terminal.see(tk.END)

    def set_cmd(self, text):
        self.cmd_entry.delete(0, tk.END)
        self.cmd_entry.insert(0, text)

    def show_dashboard(self):
        self.log("\n--- AAAYAFUJ NET DASHBOARD ---")
        self.log("[+] Engine: Operational")
        self.log("[+] Mode: Secure Desktop (GUI)")
        self.log("[+] Core Packets: Synchronized")

    def execute_command(self):
        cmd = self.cmd_entry.get().strip()
        if not cmd or self.is_running:
            return
        
        self.is_running = True
        self.run_btn.config(state=tk.DISABLED, text="RUNNING...")
        self.status_label.config(text=f"EXECUTING: {cmd}", foreground="#ef4444")
        self.log(f"\n{RED}aaayafuj > {RESET}{cmd}")
        
        threading.Thread(target=self._run_sub, args=(cmd,), daemon=True).start()

    def _run_sub(self, cmd):
        try:
            # We run via python main.py to use existing logic
            full_cmd = f'"{sys.executable}" main.py {cmd}'
            process = subprocess.Popen(full_cmd, shell=True, stdout=subprocess.PIPE, 
                                     stderr=subprocess.STDOUT, text=True, bufsize=1)
            
            for line in process.stdout:
                self.log(line.strip())
            
            process.wait()
        except Exception as e:
            self.log(f"[!] Execution Error: {e}")
        finally:
            self.is_running = False
            self.root.after(0, self._on_finish)

    def _on_finish(self):
        self.run_btn.config(state=tk.NORMAL, text="EXECUTE")
        self.status_label.config(text="READY", foreground="#666")

    def run_batch_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Batch Files", "*.bat"), ("All Files", "*.*")])
        if file_path:
            self.log(f"\n[*] Executing External Batch: {os.path.basename(file_path)}")
            threading.Thread(target=self._run_batch, args=(file_path,), daemon=True).start()

    def _run_batch(self, path):
        try:
            process = subprocess.Popen(path, shell=True, stdout=subprocess.PIPE, 
                                     stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                self.log(line.strip())
            process.wait()
            self.log("[+] Batch Execution Finished.")
        except Exception as e:
            self.log(f"[!] Batch Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AaayafujNetGUI(root)
    root.mainloop()
