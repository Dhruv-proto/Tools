# 📱 Android APK Automation Tool

This Python-based suite automates a simple, focused workflow for Android application testing:

- ✅ Opens **at least two Android emulators**
- 📦 Installs APK files into the emulators
- 🚀 Launches the installed apps
- 📸 Takes a screenshot of each launched app

All these steps are coordinated and executed by a main script.

---

## 📂 Project Scripts Overview

```
.
├── script.py         # 🔧 Main entry point that orchestrates the full workflow
├── emulator.py       # Ensures minimum of 2 emulators are running
├── run.py            # Installs APKs into the emulators
├── launch.py         # Launches APKs and captures screenshots
```

---

## 📁 Folder Setup

```
/apks              # Place your APKs here
/screenshots       # Output screenshots will be saved here
```

---

## ⚙️ Requirements

- Python 3.x
- Android SDK installed with `adb` and `emulator` in your system PATH
- At least **2 Android Virtual Devices (AVDs)** set up

---

## 🚀 How to Use

### 1. Place Your APKs
Put your `.apk` files into the `/apks` folder.

### 2. Run the Automation
Use the main script to execute the entire process:
```bash
python script.py
```
This will:
- Ensure at least 2 emulators are running
- Install the APKs
- Launch each app
- Take and save a screenshot for each

---

## 📌 Notes

- Only `.apk` files are processed.
- The script does **not** perform any analysis, logging, or data extraction beyond launching and capturing screenshots.
- Ensure the emulators are booted and unlocked for the script to work correctly, also they should not contain any other preinstalled user apks.
- put the path of emulator.exe in your environment variable to launch emulators through command prompt.(you can find this at C:\Users\YOU\AppData\Local\Android\Sdk\emulator in windows)

---

## 🧾 License

MIT License – Free for personal, academic, and research use.

