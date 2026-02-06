import os
import sys

# ========= COLORS =========
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

class HelpBot:
    def __init__(self, brain_file=None):
        if brain_file is None:
            # Locate brain.txt relative to this script's directory for package portability
            self.brain_file = os.path.join(os.path.dirname(__file__), "brain.txt")
        else:
            self.brain_file = brain_file
            
        self.knowledge = {}
        self.load_brain()

    def load_brain(self):
        if not os.path.exists(self.brain_file):
            return
        
        try:
            with open(self.brain_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Split by double newline to separate Q&A pairs
                pairs = content.strip().split('\n\n')
                for pair in pairs:
                    lines = pair.strip().split('\n')
                    if len(lines) >= 2:
                        q = ""
                        a_lines = []
                        for line in lines:
                            if line.startswith('Q:'):
                                q = line.replace('Q:', '').strip().lower()
                            elif line.startswith('A:'):
                                a_lines.append(line.replace('A:', '').strip())
                            else:
                                a_lines.append(line.strip())
                        
                        if q:
                            self.knowledge[q] = "\n".join(a_lines)
        except Exception as e:
            print(f"{YELLOW}[!] Knowledge Base Error: {e}{RESET}")

    def find_answer(self, user_query):
        query = user_query.lower().strip()
        
        if query in self.knowledge:
            return self.knowledge[query]
        
        best_match = None
        for q, a in self.knowledge.items():
            if query in q:
                return a
            words = query.split()
            if any(word in q for word in words if len(word) > 2):
                best_match = a
        
        return best_match if best_match else "I'm sorry, I don't have a specific answer for that. Try asking about 'architecture', '300 commands', 'safety', or 'scan'."

    def start(self):
        print(f"\n{CYAN}{BOLD}--- Aaayafuj AI Knowledge Assistant ---{RESET}")
        print(f"{CYAN}Deep-dive into the tool logic. Type 'exit' to return.{RESET}\n")
        
        while True:
            try:
                query = input(f"{BOLD}User:{RESET} ").strip()
                if not query:
                    continue
                if query.lower() in ('exit', 'quit', 'back'):
                    print(f"{CYAN}Returning to main console...{RESET}")
                    break
                
                answer = self.find_answer(query)
                print(f"{GREEN}{BOLD}Bot:{RESET} {answer}\n")
            except (KeyboardInterrupt, EOFError):
                print("")
                break
            except Exception as e:
                print(f"{YELLOW}[!] Error: {e}{RESET}")
