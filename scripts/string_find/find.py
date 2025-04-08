import subprocess
import os

def search_in_files(path, search_string):
    # Check if path exists
    if not os.path.exists(path):
        print("The specified path does not exist.")
        return
    
    # Modify search string to match substrings
    regex_search_string = f".*{search_string}.*"
    
    # Check if it's a file or folder
    if os.path.isfile(path):
        command = ["findstr", "/I", "/R", regex_search_string, path]
    else:
        command = ["findstr", "/S", "/I", "/R", regex_search_string, f"{path}\\*.*"]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True, encoding="utf-8", errors="ignore")
        if result.stdout:
            print("Search Results:")
            for line in result.stdout.splitlines():  # Ensuring each result is on a new line
                if line.strip():
                    print(line.strip())
        else:
            print("No matches found.")
    except Exception as e:
        print(f"Error executing command: {e}")

if __name__ == "__main__":
    path = input("Enter the path of the file or folder: ").strip()
    search_string = input("Enter the search string: ").strip()
    search_in_files(path, search_string)
