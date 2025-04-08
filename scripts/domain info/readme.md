
---

# 🌍 Domain Info Lookup Tool

This Python script takes a list of domains and fetches detailed information for each one, including IP address, registrar, registrant details, and hosting provider. Results are saved into a CSV file for further use.

---

## ✅ Features

- 🌐 Resolves domain to IP address
- 🔍 Looks up WHOIS information (registrar, registrant name/org/address/country)
- ☁️ Identifies the hosting provider via RDAP
- 📁 Outputs all data into a structured CSV file

---

## 📂 Input Format

The script expects a `.txt` file containing a list of domains, one per line:

```
example.com
google.com
openai.com
```

---

## 📤 Output

The output is saved as `domain_info.csv` and includes:

| Domain      | IP Address | Registrar | Registrant Name | Registrant Organization | Registrant Address | Registrant Country | Hosting Provider |
|-------------|------------|-----------|------------------|--------------------------|---------------------|---------------------|------------------|
| example.com | 93.184.216.34 | NameCheap | John Doe | Example Inc. | 123 Domain St. | US | Cloudflare |

---

## ⚙️ How to Use

1. Ensure you have the required libraries installed:

```bash
pip install python-whois ipwhois requests
```

2. Run the script:

```bash
python domainlookup.py
```

3. When prompted, provide the path to your domain list text file:

```
Enter the path of the text file containing domains: domainlist.txt
```

4. After processing, check `domain_info.csv` in the same folder.

---

## 🧾 Dependencies

- `socket`
- `whois`
- `ipwhois`
- `requests`
- `csv`
- `urllib.parse`

---

## 📝 Notes

- If WHOIS data is unavailable or incomplete, the script will attempt to use RDAP as a fallback.
- Error handling is built-in for cases like unresolvable domains or unavailable WHOIS info.
- Network access is required for WHOIS and RDAP queries.

---

## 🔒 License

Open-source and free to use for educational, research, or internal use.

---
