import socket
import csv
import whois
import requests
from ipwhois import IPWhois
from urllib.parse import urlparse

def get_registrar_rdap(domain):
    try:
        response = requests.get(f"https://rdap.org/domain/{domain}", timeout=10)
        data = response.json()
        for entity in data.get("entities", []):
            roles = entity.get("roles", [])
            if "registrar" in roles:
                return entity.get("vcardArray", [[{}]])[1][1]  # Extract registrar name
        return "Unknown"
    except Exception:
        return "Error retrieving"

def get_domain_info(domain_url):
    parsed_url = urlparse(domain_url)
    domain = parsed_url.netloc if parsed_url.netloc else parsed_url.path
    
    try:
        ip_address = socket.gethostbyname(domain)
    except socket.gaierror:
        ip_address = "Could not resolve"
    
    try:
        domain_info = whois.whois(domain)
        registrar = domain_info.registrar if domain_info.registrar else get_registrar_rdap(domain)
        registrant_name = domain_info.name if hasattr(domain_info, 'name') else "Unknown"
        registrant_org = domain_info.org if hasattr(domain_info, 'org') else "Unknown"
        registrant_address = domain_info.address if hasattr(domain_info, 'address') else "Unknown"
        registrant_country = domain_info.country if hasattr(domain_info, 'country') else "Unknown"
    except Exception:
        registrar = get_registrar_rdap(domain)
        registrant_name = "Error retrieving"
        registrant_org = "Error retrieving"
        registrant_address = "Error retrieving"
        registrant_country = "Error retrieving"
    
    hosting_provider = "Unknown"
    if ip_address != "Could not resolve":
        try:
            ip_info = IPWhois(ip_address).lookup_rdap()
            hosting_provider = ip_info.get("network", {}).get("name", "Unknown")
        except Exception:
            hosting_provider = "Error retrieving"
    
    print(f"{domain} info has been fetched.")
    return domain, ip_address, registrar, registrant_name, registrant_org, registrant_address, registrant_country, hosting_provider

def process_domains(file_path, output_file):
    with open(file_path, "r") as f:
        domains = [line.strip() for line in f if line.strip()]
    
    results = []
    for domain in domains:
        results.append(get_domain_info(domain))
    
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Domain", "IP Address", "Registrar", "Registrant Name", "Registrant Organization", "Registrant Address", "Registrant Country", "Hosting Provider"])
        writer.writerows(results)

    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    input_file = input("Enter the path of the text file containing domains: ")
    output_file = "domain_info.csv"
    process_domains(input_file, output_file)
