import os
import subprocess
import re

failed = []

def get_user_installed_packages(emulator):
    """Fetches all user-installed package names from the emulator."""
    print(f"Fetching user-installed packages from {emulator}...")
    try:
        package_list_output = subprocess.run(
            ["adb", "-s", emulator, "shell", "pm", "list", "packages", "-3"],
            capture_output=True, text=True
        ).stdout
        packages = [line.replace("package:", "").strip() for line in package_list_output.split("\n") if line.strip()]
        return packages
    except Exception as e:
        print(f"Error retrieving installed packages: {e}")
        return []

def launch_app_with_fallback(emulator, package_name):
    """Attempts to launch the app using 'monkey'. Falls back to alternative launch methods if needed."""
    # Attempt to launch using monkey
    result = subprocess.run(
        ["adb", "-s", emulator, "shell", "monkey", "-p", package_name, "-c", "android.intent.category.LAUNCHER", "1"],
        capture_output=True, text=True
    )

    if "monkey aborted" not in result.stdout.lower():
        return True  # Successfully launched using monkey

    print(f"Monkey failed for {package_name}, trying fallback activities...")

    # Try fallback activities
    dumpsys_output = subprocess.run(
        ["adb", "-s", emulator, "shell", "dumpsys", "package", package_name],
        capture_output=True, text=True
    ).stdout
    
    fallback_activities = re.findall(r'[A-Za-z0-9_.]+Activity[A-Za-z0-9_]*', dumpsys_output)
    
    for activity in reversed(fallback_activities):
        component_name = f"{package_name}/{activity}"
        result = subprocess.run(
            ["adb", "-s", emulator, "shell", "am", "start", "-n", component_name],
            capture_output=True, text=True
        )
        output_lower = result.stdout.lower()
        
        if "permission denial" in output_lower or "not exported" in output_lower or "security exception" in output_lower:
            print(f"Permission Denial or Security Exception encountered for {component_name}. Trying next fallback...")
            continue  # Try next fallback activity

        if "error" not in output_lower:
            print(f"Successfully launched {package_name} with {activity} on {emulator}")
            return True  # Successfully launched

    print(f"Failed to launch {package_name} on {emulator} using all fallback methods.")
    return False  # Failed to launch

def launch_and_screenshot(emulators):
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    
    if not emulators:
        print("No running emulators detected.")
        return
    
    # Create a new installed mapping by listing installed packages for the selected emulators
    installed_mapping = {}
    for emulator in emulators:
        installed_mapping[emulator] = get_user_installed_packages(emulator)
    
    for emulator, user_packages in installed_mapping.items():
        for package_name in user_packages:
            print(f"\nProcessing package: {package_name}")
            print(f"Attempting to launch {package_name} on {emulator}...")
            
            if not launch_app_with_fallback(emulator, package_name):
                print(f"Failed to launch {package_name} on {emulator}.")
                failed.append(package_name)
                continue
            print(f"{package_name} launched successfully on {emulator}...")
            # Wait for app to load
            subprocess.run(["sleep", "5"])
            
            # Take Screenshot
            screenshot_path = f"/sdcard/{package_name}.png"
            local_screenshot_path = os.path.join(screenshot_dir, f"{package_name}.png")
            try:
                subprocess.run(["adb", "-s", emulator, "shell", "screencap", "-p", screenshot_path], check=True)
                subprocess.run(["adb", "-s", emulator, "pull", screenshot_path, local_screenshot_path], check=True)
                print(f"Screenshot saved for {package_name} at {local_screenshot_path}.")
            except subprocess.CalledProcessError:
                print(f"Failed to take screenshot for {package_name} on {emulator}.")
                failed.append(package_name)

            # Close the app
            print(f"Closing {package_name} on {emulator}...")
            subprocess.run(["adb", "-s", emulator, "shell", "am", "force-stop", package_name])
    
    print("\n\nUnable to take Screenshots of Following Packages:")
    print(failed)

if __name__ == "__main__":
    print("This script should be called with a list of selected emulators from the main script.")
