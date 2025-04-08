import os
import subprocess

def list_emulators():
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    lines = result.stdout.split("\n")[1:]
    emulators = [line.split("\t")[0] for line in lines if "emulator" in line]
    return emulators

def install_apks_to_emulators(apk_folder, emulators):
    apk_files = [f for f in os.listdir(apk_folder) if f.endswith((".apk",".APK"))]

    if len(apk_files) == 0:
        print("No APK files found in the specified folder.")
        return {}, []

    if len(emulators) < 2:
        print("At least two emulators must be running.")
        return {}, []

    first_emulator, second_emulator = emulators[:2]
    installed_mapping = {}
    failed_apks = []

    for idx, apk in enumerate(apk_files[:10]):  # Process only first 10 APKs
        emulator = first_emulator if idx < 5 else second_emulator
        apk_path = os.path.join(apk_folder, apk)

        try:
            subprocess.run(["adb", "-s", emulator, "install", apk_path], check=True)
            print(f"Successfully installed {apk} on {emulator}.")
            installed_mapping[apk] = emulator
        except subprocess.CalledProcessError:
            print(f"Failed to install {apk} on {emulator}.")
            failed_apks.append(apk)

    return installed_mapping, failed_apks

if __name__ == "__main__":
    apk_folder = input("Enter the path to the APK folder: ").strip()
    emulators = list_emulators()
    
    if len(emulators) < 2:
        print("At least two emulators are required.")
        exit(1)

    install_apks_to_emulators(apk_folder, emulators)