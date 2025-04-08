import os
import hashlib
import csv

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def process_apk_files(directory):
    csv_file = os.path.join(directory, "apk_hashes.csv")
    
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["APK Name", "SHA256 Hash"])
        
        for filename in os.listdir(directory):
            if filename.endswith(".apk"):
                file_path = os.path.join(directory, filename)
                sha256_hash = calculate_sha256(file_path)
                new_filename = f"{sha256_hash}.apk"
                new_file_path = os.path.join(directory, new_filename)
                
                writer.writerow([filename, sha256_hash])
                
                os.rename(file_path, new_file_path)
                print(f"Renamed {filename} -> {new_filename}")

if __name__ == "__main__":
    dir_path = input("Enter the directory path containing APK files: ")
    if os.path.isdir(dir_path):
        process_apk_files(dir_path)
        print("Process completed. Check apk_hashes.csv in the directory.")
    else:
        print("Invalid directory path. Please try again.")
