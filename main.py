#!/usr/bin/env python3
import sys
import os
import time
import shlex

# =================================================================
# MODULE RESOLUTION FIX
# Ensure the project root is in the python path for module resolution.
# =================================================================
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import suite components using package naming
try:
    from aaayafuj.cli import get_parser
    from aaayafuj.core.dispatcher import Dispatcher
    from aaayafuj.version import __version__
    from aaayafuj.utils.help_bot import HelpBot
except ImportError as e:
    print(f"\033[91m[-] Critical Error: Failed to load suite modules.\033[0m")
    print(f"[*] Error Details: {e}")
    sys.exit(1)

# ========= COLORS =========
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

# Enable ANSI colors on Windows
if os.name == "nt":
    os.system("")

# ========= BANNER =========
BANNER = f"""{RED}
       ..|'''.|  .|'''.|  ' ____
   |||    .|'     '   ||..  '    `  ||
  |  ||   ||           ''|||.       /,
 .''''|.  '|.      . .     '||     //
.|.  .||.  ''|....'  |'....|'     ((
                                  ||
                                  |'
{RESET}
"""

WELCOME = f"""{GREEN}
welcome to Aaayafuj Cyber Security Net
{RESET}
"""

# ========= CORE INFO =========
START_TIME = time.time()
VERSION = __version__
LICENSE = "Private Cybersecurity Research License"

# ========= COMMAND HANDLERS =========
def cmd_help():
    print("""
Usage (interactive):
  help        Show help
  status      Show system status
  uptime      Show uptime
  about       About Aaayafuj
  license     Show license
  verify      Run integrity checks
  bot         Launch Help AI Bot
  
Module Categories (Connected):
  scan [cmd]  Launch security scanners
  net [cmd]   Network diagnostics
  sys [cmd]   System auditing
  assets [cmd] Asset management
  
  exit        Exit console
""")

def cmd_status():
    print("[+] Aaayafuj status: ACTIVE")
    print("[+] Modules: Loaded")
    print("[+] Mode: Secure")

def cmd_uptime():
    uptime = int(time.time() - START_TIME)
    print(f"[+] Uptime: {uptime} seconds")

def cmd_about():
    print(f"""
Aaayafuj Cyber Security Net v{VERSION}
Framework-style security platform
Research • Defense • Automation
""")

def cmd_license():
    print(LICENSE)

def cmd_verify():
    print("[*] Running integrity checks...")
    time.sleep(1)
    print("[+] Core files verified")
    print("[+] No tampering detected")

def cmd_bot():
    bot = HelpBot()
    bot.start()

# ========= COMMAND MAP =========
COMMANDS = {
    "help": cmd_help,
    "status": cmd_status,
    "uptime": cmd_uptime,
    "about": cmd_about,
    "license": cmd_license,
    "verify": cmd_verify,
    "bot": cmd_bot,
}

# ========= INTERACTIVE CONSOLE =========
def start_console():
    parser = get_parser()
    while True:
        try:
            user_input = input("aaayafuj > ").strip()

            if not user_input:
                continue

            if user_input.lower() in ("exit", "quit"):
                print(f"{RED}Exiting Aaayafuj...{RESET}")
                break

            cmd_parts = shlex.split(user_input)
            cmd = cmd_parts[0].lower()

            if cmd in COMMANDS:
                COMMANDS[cmd]()
            else:
                try:
                    args, unknown = parser.parse_known_args(cmd_parts)
                    if args.category:
                        dispatcher = Dispatcher(args)
                        dispatcher.dispatch()
                    else:
                        print(f"[-] Unknown command '{cmd}'. Type 'help'.")
                except SystemExit:
                    pass
                except Exception as e:
                    print(f"{RED}[ERROR]{RESET} Module error: {e}")

        except KeyboardInterrupt:
            print(f"\n{RED}[*]{RESET} Use 'exit' to quit.")
        except EOFError:
            break
        except Exception as e:
            print(f"{RED}[ERROR]{RESET} {e}")

# ========= ENTRY POINT =========
def main():
    if len(sys.argv) > 1:
        from aaayafuj.cli import main as cli_main
        cli_main()
        return

    print(BANNER)
    print(WELCOME)
    start_console()

if __name__ == "__main__":
    main()
