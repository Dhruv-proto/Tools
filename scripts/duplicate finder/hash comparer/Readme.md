# 🔐 Hash Comparator Script

This Python script compares **two text files containing hash values** (e.g., MD5, SHA-1, SHA-256) and identifies common hashes between them. It's especially useful for security researchers, forensic analysts, or sysadmins who need to quickly find intersecting hashes between datasets.

---

## 📌 Features

- ✅ Reads hash values from two plain text files
- 🔍 Finds **common hash values** between the files
- 📊 Prints total counts and matched entries
- 🧼 Case-insensitive and ignores duplicates

---

## 📂 Input Format

Each input file (e.g., `hashes1.txt`, `hashes2.txt`) should contain one hash per line:

```
5d41402abc4b2a76b9719d911017c592
098f6bcd4621d373cade4e832627b4f6
2fd4e1c67a2d28fced849ee1bb76e7391b93eb12
```

---

## 🧰 Requirements

- Python 3.x
- Standard Python libraries (`re`, `collections`)

---

## ⚙️ How to Use

1. Save your hash lists in two `.txt` files.
2. Update these variables in the script:

```python
file1 = "hashes1.txt"
file2 = "hashes2.txt"
```

3. Run the script:

```bash
python comphass.py
```

---

## 📤 Output

The script will display:

- Total number of **common hashes**
- Each matching hash with frequency (if duplicates exist)
- Total number of hashes in each file

**Example:**
```
Total number of common words: 3

Words present in both files with their counts:
5d41402abc4b2a76b9719d911017c592: File 1 (1), File 2 (2)
098f6bcd4621d373cade4e832627b4f6: File 1 (1), File 2 (1)
...

Word Counts in Each File:
File 1 (hashes1.txt): 25 words
File 2 (hashes2.txt): 30 words
```

---

## 📝 Notes

- Hashes are **case-insensitive**.
- Ensure the files are UTF-8 encoded and contain **one hash per line**.
- Script can be easily extended to export results to a CSV file.

---

## 🧾 License

This tool is open-source and free to use for personal, research, and non-commercial purposes.

