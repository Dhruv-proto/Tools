
---

# 🌐 IP Address Comparator

This Python script compares two text files to extract and count **IPv4 addresses**, identifying IPs common to both files along with their frequency in each. It's ideal for analyzing logs or forensic IP tracking.

---

## ✅ Features

- 📥 Reads IP addresses from two input files
- 📊 Counts frequency of each IP in both files
- 🔎 Identifies **common IPs** between the files
- 📋 Reports total IPs and shared IPs with frequency

---

## 📂 Input Format

Each input file should contain text with embedded IPv4 addresses. The script will automatically extract them using regular expressions.

**Example (ip1.txt):**
```
User logged in from 192.168.1.10
Attempt from 8.8.8.8 failed
```

**Example (ip2.txt):**
```
Connection established with 192.168.1.10
Another access by 1.1.1.1
```

---

## ⚙️ How to Use

1. Place your two IP-containing text files in the same directory.
2. Update the filenames in the script:
   ```python
   file1 = "ip2.txt"
   file2 = "ip1.txt"
   ```
3. Run the script:
   ```bash
   python ipcompare.py
   ```

---

## 📤 Output

**Example Output:**
```
Total number of common IPs: 1

IP addresses present in both files with their counts:
192.168.1.10: File 1 (1), File 2 (1)

IP Counts in Each File:
File 1 (ip2.txt): 2 IPs
File 2 (ip1.txt): 2 IPs
```

---

## 🧰 Requirements

- Python 3.x
- No external libraries (uses built-in `re` and `collections`)

---

## 📝 Notes

- Only IPv4 addresses are supported.
- The script ignores duplicates in its final common IP list but shows frequencies.
- Ensure your files are encoded in UTF-8 and contain IPs in standard dotted-decimal format.

---

## 🧾 License

Free for educational, research, and non-commercial use.

---
