# Aaayafuj Cybersecurity Suite 7

A modular, high-performance Python ecosystem for security auditing, network scanning, and system integrity verification.

## 🚀 NEW: AAAYAFUJ NET (Desktop GUI)
For a full visual experience, run the advanced Desktop UI:
```bash
python Net.py
```
**Features:**
- Real-time terminal output.
- Module navigation sidebar.
- **Batch (.bat) Runner**: Execute external automation scripts directly.
- Modern dark-theme interface.

---

## ⚠️ CRITICAL: FIX FOR WINDOWS "FATAL ERROR"
If you see `Fatal error in launcher: Unable to create process...` when running `pip`, **DO NOT PANIC**. Your Python installation is fine, but the Windows pip launcher is broken.

**The Fix:** Always use `python -m pip` instead of `pip`.

```powershell
# WRONG (will likely fail on Windows)
pip install .

# RIGHT (always works)
python -m pip install .
```

---

## 🚩 GITHUB ACCOUNT SUSPENDED?
If you see `remote: Your account is suspended` when cloning:
1. This is a **GitHub platform issue**, not a bug in Aaayafuj.
2. Visit [https://support.github.com](https://support.github.com) immediately.
3. Check your email for a "Notice of Suspension" from GitHub.
4. Once GitHub clears your account, the `git clone` command will work again.

---

## Installation

```bash
# 1. Clone (Latest Official Repository)
git clone https://github.com/aaayafuj51-AYFJ/Aaayafuja_CyberSecurity7.py.git
cd Aaayafuja_CyberSecurity7.py

# 2. Install Dependencies safely
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# 3. Install the Tool
python -m pip install .
```

## Usage Modes

### 1. Advanced GUI (Net.py)
```bash
python Net.py
```

### 2. Interactive CLI Console
```bash
aaayafuj
```

### 3. Quick Commands
- `aaayafuj doctor`: Run environment diagnostics.
- `aaayafuj bot`: Launch the AI Help Assistant.
- `aaayafuj verify`: Check tool integrity.

## Troubleshooting Logic
If the tool won't start, run the doctor directly:
```bash
python aaayafuj/utils/env_check.py
```