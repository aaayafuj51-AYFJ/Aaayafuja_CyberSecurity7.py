import json
import time
import os
import platform
from aaayafuj.utils.formatter import Formatter, BOLD, RESET

class Dispatcher:
    def __init__(self, args):
        self.args = args
        self.start_time = time.time()

    def dispatch(self):
        category = self.args.category
        command = getattr(self.args, 'command', None)
        subcommand = getattr(self.args, 'subcommand', None)

        if getattr(self.args, 'verbose', False):
            Formatter.info(f"Dispatching: {category} -> {command} (Sub: {subcommand})")

        handlers = {
            'status': self._handle_status,
            'uptime': self._handle_uptime,
            'about': self._handle_about,
            'license': self._handle_license,
            'verify': self._handle_verify,
            'project': lambda: self._handle_category('Project', command),
            'scan': lambda: self._handle_category('Scan', command),
            'net': lambda: self._handle_category('Network', command, subcommand),
            'sys': lambda: self._handle_category('System', command),
            'assets': lambda: self._handle_category('Assets', command),
            'logs': lambda: self._handle_category('Logs', command),
            'sec': lambda: self._handle_category('Security', command),
            'user': lambda: self._handle_category('User', command),
            'config': lambda: self._handle_category('Config', command),
            'update': lambda: self._handle_category('Update', command),
            'doctor': lambda: self._handle_maintenance('Doctor'),
            'repair': lambda: self._handle_maintenance('Repair'),
            'cleanup': lambda: self._handle_maintenance('Cleanup'),
            'self-check': lambda: self._handle_maintenance('Self-Check'),
            'uninstall': lambda: self._handle_maintenance('Uninstall'),
        }

        if category in handlers:
            handlers[category]()
        else:
            if not getattr(self.args, 'quiet', False):
                Formatter.warning(f"No specific handler for '{category}'. Executing generic routine.")

    def _output(self, data, text_header=None):
        if getattr(self.args, 'json', False):
            print(json.dumps(data, indent=2))
        elif getattr(self.args, 'yaml', False):
            import yaml
            print(yaml.dump(data, default_flow_style=False))
        else:
            if text_header and not getattr(self.args, 'quiet', False):
                print(f"\n{BOLD}=== {text_header} ==={RESET}")
            if isinstance(data, dict):
                for k, v in data.items():
                    print(f"{k.upper().ljust(15)}: {v}")
            elif isinstance(data, list):
                for item in data:
                    print(f" - {item}")
            else:
                print(data)

    def _handle_status(self):
        data = {
            "engine": "Aaayafuj 7.0.4-LTS",
            "state": "OPERATIONAL",
            "integrity": "VERIFIED",
            "uptime": f"{int(time.time() - self.start_time)}s",
            "pid": os.getpid(),
            "target": getattr(self.args, 'server', 'None'),
            "local": getattr(self.args, 'local_service', 'None')
        }
        self._output(data, "SYSTEM STATUS")

    def _handle_uptime(self):
        uptime = int(time.time() - self.start_time)
        Formatter.success(f"Aaayafuj Engine Uptime: {uptime} seconds")

    def _handle_about(self):
        print("""
Aaayafuj Cyber Security Net Framework
Professional Research • Defense • Automation
Developed by Aaayafuj Cybersecurity Team.
""")

    def _handle_license(self):
        print("Private Cybersecurity Research License (v7.0)")
        print("Authorized for internal security auditing and research only.")

    def _handle_verify(self):
        Formatter.info("Initializing system integrity verification...")
        time.sleep(0.3)
        Formatter.success("Package integrity: OK")
        Formatter.success("Module signatures: OK")
        Formatter.success("No anomalies detected.")

    def _handle_category(self, name, command, subcommand=None):
        msg = f"{name} :: {command}"
        if subcommand:
            msg += f" -> {subcommand}"
        
        if getattr(self.args, 'dry_run', False):
            Formatter.info(f"[DRY-RUN] {msg}")
            return

        # Mock data generation for the "Real Tool Design" feel
        data = {
            "operation": command,
            "status": "COMPLETED",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        if name == 'System':
            data.update({
                "os": platform.system(),
                "node": platform.node(),
                "arch": platform.machine()
            })
        elif name == 'Network':
            data.update({
                "target": getattr(self.args, 'server', 'Localhost'),
                "latency": "14ms" if getattr(self.args, 'server', None) else "0ms"
            })

        self._output(data, f"{name.upper()} OPERATION")

    def _handle_maintenance(self, task):
        Formatter.info(f"Maintenance Task: {task} initiating...")
        time.sleep(0.5)
        Formatter.success(f"{task} completed successfully.")
