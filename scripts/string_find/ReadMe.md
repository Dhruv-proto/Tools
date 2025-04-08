
---

# 🔍 Find String in Files – Python Utility

This is a simple Python script that allows you to **search for a string or pattern** within a file or recursively through all files in a directory on a **Windows** system. It leverages the built-in `findstr` command for efficient text searching.

## 📁 Features

- ✅ Search within a single file or across an entire folder.
- 🔎 Case-insensitive and regex-enabled matching.
- 🖥️ Uses Windows `findstr` command for performance and compatibility.
- 🧵 Outputs clean, line-by-line search results.

## 📌 Requirements

- Python 3.x
- Windows OS (script uses the `findstr` command specific to Windows)

## 🚀 Usage

1. Open a terminal or command prompt.
2. Run the script using Python:
   ```bash
   python find.py
   ```

3. You will be prompted to:
   - **Enter the path** of a file or directory.
   - **Enter the search string** you want to find.

4. The script will display all matching lines.

## 📂 Example

```
Enter the path of the file or folder: C:\Users\You\Documents
Enter the search string: error
```

It will recursively search through all files under `Documents` for any lines containing the word “error” (case-insensitive).

## ⚠️ Notes

- This script is intended for **Windows** only. If you need a cross-platform version, consider using `grep` on Unix-based systems.
- Make sure the path you provide is valid and accessible.
- Regex patterns are supported as the search string thanks to `findstr /R`.

## 🛠️ Error Handling

- If the path does not exist, you’ll get a warning message.
- If the command fails, the script will display the error for debugging.

## 🧾 License

This script is provided as-is, without warranty. You are free to use and modify it.

---
