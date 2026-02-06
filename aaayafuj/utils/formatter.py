import os

# ========= COLORS =========
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Enable ANSI colors on Windows
if os.name == "nt":
    os.system("")

BANNER = f"""{RED}
       ..|'''.|  .|'''.|  ' ____
   |||    .|'     '   ||..  '    `  ||
  |  ||   ||           ''|||.       /,
 .''''|.  '|.      . .     '||     //
.|.  .||.  ''|....'  |'....|'     ((
                                  ||
                                  |'
{RESET}{BOLD}
 Aaayafuj Cybersecurity Suite v7.0.4-LTS
 Professional Research & Defense Framework
{RESET}"""

class Formatter:
    @staticmethod
    def banner():
        print(BANNER)

    @staticmethod
    def welcome():
        print(f"{GREEN}welcome to Aaayafuj Cyber Security Net{RESET}\n")

    @staticmethod
    def info(text):
        print(f"{BLUE}[*]{RESET} {text}")

    @staticmethod
    def success(text):
        print(f"{GREEN}[+]{RESET} {text}")

    @staticmethod
    def error(text):
        print(f"{RED}[!]{RESET} {text}")

    @staticmethod
    def warning(text):
        print(f"{YELLOW}[?]{RESET} {text}")
