---

# 📦 APK SHA256 Hasher and Renamer

This script automates the process of calculating **SHA-256 hashes** for APK files in a given directory. It renames each APK to its corresponding hash and logs all results into a CSV file for easy reference.

---

## 🚀 Features

- 🔐 Calculates SHA-256 hash for each `.apk` file
- 📝 Logs original APK filenames and hashes to `apk_hashes.csv`
- 🔁 Renames each APK file to its hash value (`<hash>.apk`)
- ✅ Easy to use via command line

---

## 📁 Input Format

Place your `.apk` files in a folder of your choice. The script will process every `.apk` file in that directory.

**Example Directory:**

```
/apks
├── app1.apk
├── app2.apk
└── game.apk
```

---

## 📤 Output

For each `.apk` file:
- It will be renamed to its SHA-256 hash (e.g., `f2ab3...8c.apk`)
- A file `apk_hashes.csv` will be created in the same directory:

**CSV Format:**

| APK Name  | SHA256 Hash                          |
|-----------|--------------------------------------|
| app1.apk  | f2ab3c66f9933d1c6818c3f4a1fa...c12d  |
| game.apk  | 48e3a115ce9fa56d5dd994a15be8...05af  |

---

## ⚙️ How to Use

1. Run the script:
   ```bash
   python hashing.py
   ```

2. When prompted, enter the full path to the directory containing `.apk` files:
   ```
   Enter the directory path containing APK files: C:\Users\You\Downloads\apks
   ```

3. That's it! The APKs will be renamed and logged.

---

## 🧾 Notes

- The script only processes files with `.apk` extension.
- If an APK with the hash name already exists, it may be overwritten (use caution).
- Make sure you have write permissions in the specified folder.

---

## 📌 Requirements

- Python 3.x
- No external dependencies required

---

## 📝 License

Free to use, modify, and distribute for personal and educational use.

---
