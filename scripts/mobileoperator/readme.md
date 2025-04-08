

---

# 📞 Mobile Number Operator Lookup Script

This Python script uses the [APILayer Number Verification API](https://apilayer.com/marketplace/number_verification-api) to validate phone numbers and retrieve details such as the **carrier/operator** and **location**. It reads a list of phone numbers from a text file and writes the results to a CSV file.

---

## 🚀 Features

- 🔍 Validates phone numbers via the Number Verification API.
- 📡 Retrieves the **operator** and **location** of each number.
- 📄 Reads from a plain text file and writes to a clean CSV output.
- ✅ Handles invalid numbers and API errors gracefully.

---

## 🧰 Requirements

- Python 3.x
- `requests` library (install via `pip install requests`)
- An API key from [APILayer](https://apilayer.com/marketplace/number_verification-api)

---

## 📂 Input Format

Create a file named `mb.txt` with **one phone number per line**:

```
+14158586273
+447911123456
+918527864321
```

---

## 📤 Output

After running, it generates a CSV file named `mobile_info.csv` like this:

| Phone Number     | Operator     | Location     |
|------------------|--------------|--------------|
| +1 415-858-6273  | AT&T         | California   |
| +44 7911 123456  | Vodafone UK  | United Kingdom |
| +91 8527864321   | Airtel       | India        |

---

## ⚙️ How to Use

1. Install dependencies:
   ```bash
   pip install requests
   ```

2. Replace the API key in the script:
   ```python
   api_key = "YOUR_API_KEY"
   ```

3. Run the script:
   ```bash
   python run.py
   ```

---

## 🧾 Notes

- Make sure the `mb.txt` file exists in the same directory as the script.
- Ensure your API key has enough quota for the number of lookups.
- If the number is invalid or the API request fails, it will be marked as `"Invalid"` or `"Error"`.

---

## 🔐 Security

> Do **not** hard-code your API key in production. Consider using environment variables or a secure secrets manager.

---

## 📝 License

This project is open-source and free to use for educational or non-commercial purposes.

---
