# 🔒 RansomSim: Ransomware Attack Simulator

**RansomSim** is an educational Streamlit-based tool that simulates a ransomware attack in a safe and controlled environment.

It encrypts selected file types in a chosen folder and displays a simulated ransom message, a terminal-style log, a progress bar, and live ransomware-related news from trusted cybersecurity sources.

---

## 📦 Features

- ✅ File browser (enter path manually)
- 🔐 Encrypt/Decrypt files with Fernet encryption
- 📂 Filter encryption by selected file types (e.g., `.txt`, `.jpg`, `.mp4`)
- ✅ "Select All" file types option
- ⏳ Encryption/Decryption progress bar
- 📜 Expandable terminal log
- 💰 Simulated ransom popup/message
- 📡 Live ransomware news from:
  - The Hacker News
  - Rapid7
  - ThreatPost
  - Kaspersky SecureList
- 🛡️ Educational: Safe for labs and demo purposes

---

## 📁 Supported File Types

- `.txt`, `.pdf`, `.docx`, `.csv`, `.json`, `.xml`
- `.jpg`, `.png`, `.mp3`, `.mp4`
- `.xlsx`, `.pptx`
- `.html`, `.css`, `.js`

You can easily extend this list inside `app.py`.

---

## ⚙️ Installation

1. **Install Dependencies**
 ```bash
 pip install -r requirements.txt
 ```
2. **Install Dependencies**
```bash
streamlit run app.py
```

---

## 🔐 Safety Notice
1.This is strictly a simulation.

2.It only encrypts files in a user-selected folder.

3.No real threats, spreading, or persistence.

4.Always use sample files, never sensitive data.

---

## ⚠️Legal Notice:
This tool is intended only for authorized testing and educational purposes.
