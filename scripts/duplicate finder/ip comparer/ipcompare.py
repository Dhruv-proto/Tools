import re
from collections import Counter

def get_ip_counts(file_path):
    """Extracts IP addresses and counts their occurrences in a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'  # Matches IPv4 addresses
    ips = re.findall(ip_pattern, text)  # Extract IP addresses
    return Counter(ips)  # Returns a dictionary with IP counts

def find_common_ips(file1, file2):
    ip_counts_file1 = get_ip_counts(file1)
    ip_counts_file2 = get_ip_counts(file2)

    common_ips = set(ip_counts_file1.keys()) & set(ip_counts_file2.keys())  # IPs in both files

    print("\nTotal number of common IPs:", len(common_ips))

    if common_ips:
        print("\nIP addresses present in both files with their counts:")
        for ip in common_ips:
            print(f"{ip}: File 1 ({ip_counts_file1[ip]}), File 2 ({ip_counts_file2[ip]})")
    else:
        print("\nNo common IPs found between the two files.")

    print("\nIP Counts in Each File:")
    print(f"File 1 ({file1}): {sum(ip_counts_file1.values())} IPs")
    print(f"File 2 ({file2}): {sum(ip_counts_file2.values())} IPs")

# Example Usage:
file1 = "ip2.txt"  # Replace with actual file name
file2 = "ip1.txt"  # Replace with actual file name
find_common_ips(file1, file2)
