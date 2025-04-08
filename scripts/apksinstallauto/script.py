import os
import subprocess
from run import install_apks_to_emulators
from launch import launch_and_screenshot, launch_app_with_fallback,failed
from emulator import ensure_minimum_emulators  # Import new emulator script

def main():
    # Ensure at least two emulators are running
    emulators = ensure_minimum_emulators()

    apk_folder = input("Enter the path to the folder containing APKs: ").strip()
    if not os.path.exists(apk_folder):
        print("Invalid folder path.")
        exit(1)

    installed_mapping, failed_apks = install_apks_to_emulators(apk_folder, emulators)

    print("\nInstallation Summary:")
    for apk, emulator in installed_mapping.items():
        print(f"{apk} installed on {emulator}")

    if failed_apks:
        print("\nAPK files that could not be installed:")
        print("\n".join(failed_apks))

    launch_and_screenshot(emulators)

if __name__ == "__main__":
    main()
