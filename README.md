# Aaayafuj Cybersecurity Suite 7 (ACS7)

![Aaayafuj Interactive Console](https://github.com/user-attachments/assets/13966a9b-b99d-4278-9b52-71db0c10017e)

**Aaayafuj Cybersecurity Suite 7** is a modular, high-performance Python framework engineered for advanced security research, system auditing, and network defense automation. Version 7.0.4-LTS introduces a dual-interface ecosystem: a high-fidelity Interactive CLI and the advanced **Net.py** Desktop GUI.

---

## 🚀 Two Ways to Operate

### 1. Advanced Desktop GUI (Net.py)
A full Python window interface designed for users who prefer visual management and automated batch processing.
```bash
python Net.py
```
*   **Visual Terminal**: Integrated real-time output console.
*   **Batch Runner**: One-click execution for `.bat` and automation scripts.
*   **Module Sidebar**: Quick access to all 300+ command paths.

### 2. Interactive CLI Console
The professional shell experience (as seen in the screenshot above) with combinational command logic.
```bash
python main.py
# or if installed via pip:
aaayafuj
```
*   **Combinational Logic**: Access over 300+ command variations using the `category [cmd] [sub]` structure.
*   **Interactive Shell**: Sandboxed environment with persistent session state and dedicated `bot` assistant.

---

## 🛠️ Installation & Setup

### 📥 1. Clone the Repository
```bash
git clone https://github.com/aaayafuj51-AYFJ/Aaayafuja_CyberSecurity7.py.git
cd Aaayafuja_CyberSecurity7.py
```

### 🐍 2. Safe Dependency Installation
To avoid common Windows path errors, always use the module-invocation method:
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install .
```

---

## ⚠️ Troubleshooting & Fixes

### 🚩 "Fatal error in launcher" (Windows Fix)
If you see `Unable to create process using...` when running `pip`, your Windows path handlers are out of sync. 
**The Fix:** Never type `pip`. Always type `python -m pip`.

### 🚩 GitHub Account Suspension
If `git clone` returns a **403 Forbidden** or **Suspension Error**:
1. This is a GitHub platform filter, not a tool bug.
2. Visit [support.github.com](https://support.github.com) to restore access.
3. Once restored, the repository will be accessible immediately.

---

## 🧠 Combinational Command Architecture
ACS7 doesn't just provide 300 tools; it provides a **Combinational Framework**. By mixing categories, commands, and flags, you unlock a massive operational surface:

| Category | Description | Examples |
| :--- | :--- | :--- |
| `scan` | Security & Integrity Scanners | `scan malware`, `scan integrity --full` |
| `net` | Network Diagnostics & TLS | `net info`, `net tls-check`, `net dns` |
| `sys` | System Auditing & Health | `sys info`, `sys kernel`, `sys processes` |
| `assets` | Cryptographic Asset Management | `assets hash`, `assets sign`, `assets verify` |
| `sec` | Compliance & Policies | `sec audit`, `sec baseline`, `sec status` |

---

## 🤖 AI Knowledge Assistant
Stuck? Ask the **HelpBot**. ACS7 includes an AI-driven knowledge base designed to explain architectural choices, tool logic, and professional usage.
```bash
aaayafuj > bot
```

---

## ⚖️ License
**Private Cybersecurity Research License (v7.0)**
This software is intended for authorized security auditing, academic research, and system hardening only. Misuse of this tool for unauthorized activities is strictly prohibited.

**Developed by Aaayafuj Cybersecurity Team.**