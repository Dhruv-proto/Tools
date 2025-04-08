import requests
import csv

def get_operator(phone_number, api_key):
    api_url = f"https://api.apilayer.com/number_verification/validate?number={phone_number}"
    headers = {
        "apikey": api_key
    }

    try:
        response = requests.get(api_url, headers=headers)
        data = response.json()

        if response.status_code == 200 and data['valid']:
            return {
                'Phone Number': data['international_format'],
                'Operator': data['carrier'],
                'Location':data['location']
            }
        else:
            return {'Phone Number': phone_number, 'Operator': 'Invalid','Location': 'Invalid'}

    except Exception as e:
        print(f"Error: {e}")
        return {'Phone Number': phone_number, 'Operator': 'Error', 'Location': 'Error'}

def process_numbers(input_file, output_file, api_key):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Phone Number', 'Operator', 'Location']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for line in infile:
            phone_number = line.strip()
            if phone_number:
                info = get_operator(phone_number, api_key)
                writer.writerow(info)
                print(f"Processed: {phone_number}")

if __name__ == "__main__":
    input_file = "mb.txt"
    output_file = "mobile_info.csv"
    api_key = "ikL37rNYsRu1Wpxt3Ry4dC4kRk5RPLtN"

    process_numbers(input_file, output_file, api_key)
    print(f"Processing completed. Data saved to {output_file}")
