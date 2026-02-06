# Aaayafuj Cybersecurity Suite 7

A modular, high-performance Python CLI toolset for security auditing, network scanning, and system integrity verification. Designed for professional researchers and security enthusiasts.

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