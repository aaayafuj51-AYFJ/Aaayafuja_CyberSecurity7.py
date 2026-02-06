# Aaayafuj Cybersecurity Suite 7

* A modular, high-performance Python CLI toolset for security auditing, network scanning, and system integrity verification. Designed for professional researchers and security enthusiasts.
<img width="798" height="420" alt="Screenshot 2026-02-05 233755" src="https://github.com/user-attachments/assets/ce9bb3f9-5bf7-4e6f-8ac7-29b155cc025e" />

## Features

- **Metasploit-style Console**: Interactive shell for fast module execution.
- **300+ Commands**: Comprehensive coverage of Network, System, and Security domains.
- **Modern Packaging**: Ready for deployment via GitHub or local installation.
- **Multi-platform**: Compatible with Windows, Linux, and macOS.

## Installation

```bash
# Clone the repository
git clone https://github.com/aaayafuj51-AYFJ/Aaayafuj_Cybersecurity7.git
cd Aaayafuj_Cybersecurity7

# Install using pip (standard)
pip install .

# Or install for development
pip install -e .
```

## Usage

### Interactive Mode (Metasploit-style)
Simply run the command with no arguments:
```bash
aaayafuj
```

### Direct CLI Usage
```bash
aaayafuj scan all
aaayafuj net info -s 192.168.1.1
aaayafuj sys cpu --json
```

### Flags
- `-s <ip>`: Set target server address
- `-Ls <port>`: Set local listener port
- `--json`: Output results in JSON format
- `--verbose`: Enable detailed logging

## Troubleshooting: Windows Pip Errors

If you encounter a **"Fatal error in launcher: Unable to create process..."** error when trying to run `pip install`, it usually means your Windows pip launcher is broken or the Python installation paths have changed. Follow these steps to fix it:

### Step 1: Check your Python installation
Open a new PowerShell or CMD and run:
```powershell
python --version
where python
```
You should see a valid path to `python.exe`. If not, your PATH variable needs updating.

### Step 2: Fix pip using the Python module
If `pip` directly fails, use the Python module runner to repair it:
```powershell
python -m ensurepip --upgrade
python -m pip --version
```

### Step 3: Install packages using the module method
Instead of calling `pip` directly, always use `python -m pip` on Windows to bypass launcher issues:
```powershell
python -m pip install --upgrade pip
python -m pip install rich requests colorama
```

### Step 4: Verify installation
```powershell
python -m pip show rich
python -m pip show requests
python -m pip show colorama
```

### Step 5: Environment Variables (Manual Path Fix)
If errors persist, ensure these paths are in your **System Environment Variables -> PATH**:
- `C:\Users\<YourUser>\AppData\Local\Programs\Python\Python314\`
- `C:\Users\<YourUser>\AppData\Local\Programs\Python\Python314\Scripts\`

**✅ TL;DR:**
If `pip` is broken, always use:
`python -m pip install <package>`
This directly invokes the pip module within your current Python environment and ignores the broken standalone launcher.

** Aaayafuj Cybersecurity Suite 7 is a professional-grade, modular command-line interface (CLI) framework developed for advanced security research, system auditing, and network defense automation. Engineered with a "security-first" philosophy, it provides a unified environment that bridges the gap between raw system tools and high-level security orchestration.
# 🏗️ Architectural Overview
   * The suite is built using a layered dispatch architecture, ensuring that core engine logic is separated from command implementation.
   * This allows the tool to scale to 300+ command combinations without sacrificing performance or maintainability.
   * The Gateway (main.py & cli.py): A robust entry point that handles environment validation, path resolution (especially for Windows environments), and global flag parsing (-s for targets, -Ls for listeners).
   * The Command Dispatcher: A central routing hub that translates CLI arguments into modular operations across eight distinct security domains.
   * Interactive Shell (console.py): A sandboxed terminal environment mimicking the workflow of professional frameworks like Metasploit, featuring real-time status monitoring and cross-module command execution.

#🛡️ Functional Domains
   * Aaayafuj 7 organizes its capabilities into specialized sub-engines:
   * Scan Engine: Performs deep filesystem integrity checks, malware signature analysis, and permission auditing.
   * Network Engine: Diagnostic suite for TLS verification, DNS health, and port management.
   * System Engine: Provides low-level telemetry including kernel health, process isolation, and environmental hardening.
   * Asset Engine: Manages cryptographic integrity via SHA-256 hashing and secure asset signing.
   * Security & Compliance: Validates systems against baseline hardening policies and sandbox configurations.

# 🤖 Intelligent Assistance
   * Integrated into the core utility package is the Aaayafuj AI Knowledge Assistant (HelpBot). Unlike standard help menus, the bot utilizes a structured knowledge base (brain.txt) to provide step-by-step reasoning for tool logic, architectural deep-dives, and professional usage guidance.
# 💎 Professional Standards
   * Integrity Focused: Includes built-in self-diagnostic tools (self-check, doctor, verify) to ensure the tool hasn't been tampered with.
   * Windows Optimized: Specifically addressed the common "Fatal error in launcher" issues by providing a standardized module-invocation path (python -m pip).
   * Aesthetic CLI: Utilizes ANSI styling and high-fidelity banners to provide a premium user experience within a text-only interface.
   * This framework is not just a collection of scripts; it is a complete ecosystem for security professionals who require reliability, modularity, and depth in their defensive operations.
