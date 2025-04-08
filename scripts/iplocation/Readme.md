
---

# 🌍 IP Geolocation Extractor

This Python script extracts IP addresses from a text file and retrieves their **latitude and longitude** using the **MaxMind GeoLite2 City database**. The results are saved into a CSV file for further analysis or visualization.

---

## 🚀 Features

- 🧠 Automatically extracts IPs from raw text using regex.
- 🌐 Uses MaxMind's GeoLite2 City database for accurate geolocation.
- 📝 Outputs results in a CSV file with IP, latitude, and longitude.
- ✅ Gracefully handles missing or invalid data.

---

## 🧰 Requirements

- Python 3.x
- Libraries:
  - `geoip2`
  - `csv`
  - `re`
- MaxMind **GeoLite2-City.mmdb** database (download from [MaxMind](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data))

Install dependencies:

```bash
pip install geoip2
```

---

## 📂 Input File

Create a file named `ip.txt` and paste your raw text or list of IP addresses. The script will automatically extract all valid IPs.

**Example:**
```
User 1 - 192.168.1.1
User 2 - 8.8.8.8
Failed login from 172.217.3.110
```

---

## 📤 Output

The script generates a CSV file named `ip_location_updated.csv` with the following format:

| IP Address     | Latitude | Longitude |
|----------------|----------|-----------|
| 8.8.8.8        | 37.751   | -97.822   |
| 172.217.3.110  | 37.423   | -122.083  |

If geolocation fails, coordinates are set to `"0", "0"`.

---

## ⚙️ Usage

1. Download the `GeoLite2-City.mmdb` and place it in the same directory.
2. Ensure `ip.txt` contains IPs or text with IPs.
3. Run the script:
   ```bash
   python test.py
   ```

---

## ⚠️ Notes

- You must sign up and agree to MaxMind’s licensing terms to download the database.
- Internal/reserved IPs (e.g., `192.168.x.x`) won't return accurate location data.
- Make sure the `GeoLite2-City.mmdb` path in the script matches your setup.

---

## 🧾 License

This script is provided for educational and research purposes.

---
