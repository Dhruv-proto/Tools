import geoip2.database
import csv
import re

# Path to the GeoLite2 City database (download from MaxMind)
DATABASE_PATH = 'GeoLite2-City.mmdb'

# Function to get geolocation for an IP address
def get_geolocation(ip, reader):
    try:
        response = reader.city(ip)
        return response.location.latitude, response.location.longitude
    except Exception as e:
        print(f"Error for IP {ip}: {e}")
        return "0", "0"

# Read IP addresses from the file
with open('ip.txt', 'r') as file:
    content = file.read()

# Extract IP addresses using regex
ip_addresses = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', content)

# Initialize GeoIP2 reader
reader = geoip2.database.Reader(DATABASE_PATH)

# Output CSV file
output_file = 'ip_location_updated.csv'

# Write to CSV
with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['IP Address', 'Latitude', 'Longitude'])

    for ip in ip_addresses:
        lat, lon = get_geolocation(ip, reader)
        print(f"Processing: {ip} -> {lat}, {lon}")
        csvwriter.writerow([ip, lat, lon])

reader.close()
print(f"Geolocation data saved to {output_file}")
