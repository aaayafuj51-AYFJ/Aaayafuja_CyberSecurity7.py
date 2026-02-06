import sys
import shlex
import os
import time
from aaayafuj.utils.formatter import Formatter, RED, GREEN, BLUE, RESET, BOLD
from aaayafuj.core.dispatcher import Dispatcher

# Robust package import for HelpBot
try:
    from aaayafuj.utils.help_bot import HelpBot
except ImportError:
    HelpBot = None

class InteractiveConsole:
    def __init__(self, global_args):
        self.global_args = global_args
        target = getattr(global_args, 'server', None) if global_args else None
        self.prompt_prefix = f"({RED}{target}{RESET}) " if target else ""
        self.start_time = time.time()
        
    @property
    def prompt(self):
        return f"{self.prompt_prefix}{BOLD}aaayafuj{RESET} > "
        
    def start(self):
        Formatter.banner()
        Formatter.welcome()
        print(f"[*] Type {BOLD}'help'{RESET} for commands or {BOLD}'exit'{RESET} to quit.\n")
        
        while True:
            try:
                line = input(self.prompt).strip()
                if not line:
                    continue
                
                cmd_parts = shlex.split(line)
                cmd_name = cmd_parts[0].lower()

                if cmd_name in ("exit", "quit"):
                    print(f"{RED}[*] Terminating Aaayafuj session...{RESET}")
                    break
                
                if cmd_name in ("clear", "cls"):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

                if cmd_name == "status":
                    print("[+] Aaayafuj status: ACTIVE")
                    continue
                if cmd_name == "uptime":
                    print(f"[+] Uptime: {int(time.time() - self.start_time)} seconds")
                    continue
                if cmd_name == "help":
                    self._show_help()
                    continue
                if cmd_name == "bot":
                    if HelpBot:
                        bot = HelpBot()
                        bot.start()
                    else:
                        print(f"{RED}[!] Error: HelpBot module not found in package.{RESET}")
                    continue

                self._execute_interactive_cmd(cmd_parts)

            except KeyboardInterrupt:
                print(f"\n{BLUE}[*] Interrupt received. Type 'exit' to close session.{RESET}")
            except EOFError:
                break
            except Exception as e:
                Formatter.error(f"Console Error: {e}")

    def _show_help(self):
        print(f"""
{BOLD}Core Commands:{RESET}
  status      Show system status
  uptime      Show engine uptime
  bot         Ask the AI Help Bot
  about       About Aaayafuj
  license     Show license info
  verify      Run integrity checks
  clear       Clear terminal
  exit        Exit session

{BOLD}Module Categories:{RESET}
  project     Workspace management
  scan        Security scanners
  net         Network diagnostics
  sys         System auditing
  assets      File & asset management
  logs        Log analytics
  sec         Security compliance
  user        Access control

{BOLD}Example:{RESET}
  aaayafuj > net info
  aaayafuj > scan malware
""")

    def _execute_interactive_cmd(self, parts):
        from aaayafuj.cli import get_parser
        parser = get_parser()
        try:
            args, unknown = parser.parse_known_args(parts)
            if self.global_args:
                args.server = getattr(self.global_args, 'server', args.server)
                args.local_service = getattr(self.global_args, 'local_service', args.local_service)
            
            if args.category:
                dispatcher = Dispatcher(args)
                dispatcher.dispatch()
            else:
                print(f"[-] Unknown command. Type 'help'.")
        except SystemExit:
            pass
