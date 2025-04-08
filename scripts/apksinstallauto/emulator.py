#launch android emulator
import subprocess
import time

def list_running_emulators():
    """Returns a list of running emulator device IDs."""
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    lines = result.stdout.split("\n")[1:]
    return [line.split("\t")[0] for line in lines if "emulator" in line]

def list_available_avds():
    """Returns a list of available AVDs on the system."""
    result = subprocess.run(["emulator", "-list-avds"], capture_output=True, text=True)
    return result.stdout.strip().split("\n")

def start_emulator(avd_name):
    """Starts an emulator and waits for it to boot."""
    subprocess.Popen(["emulator", "-avd", avd_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Starting emulator: {avd_name}...")
    
    # Wait for emulator to show up in ADB devices
    while True:
        time.sleep(5)
        running_emulators = list_running_emulators()
        if running_emulators:
            print(f"Emulator {avd_name} is now running.")
            break
        print("Waiting for emulator to fully start...")

def ensure_minimum_emulators():
    """Ensures at least two emulators are running, prompting the user if necessary."""
    running_emulators = list_running_emulators()

    if len(running_emulators) >= 2:
        return running_emulators

    available_avds = list_available_avds()
    if not available_avds:
        print("No available AVDs found. Please create an AVD first.")
        exit(1)

    while len(running_emulators) < 2:
        print("\nAvailable AVDs:")
        for idx, avd in enumerate(available_avds, start=1):
            print(f"{idx}. {avd}")

        choice = input(f"Select an AVD to start (1-{len(available_avds)}): ").strip()
        if not choice.isdigit() or int(choice) not in range(1, len(available_avds) + 1):
            print("Invalid selection. Try again.")
            continue

        start_emulator(available_avds[int(choice) - 1])
        running_emulators = list_running_emulators()

        # If only one emulator is running, give another chance to start another one
        if len(running_emulators) == 1:
            print("\nYou need at least two emulators running.")
            print("Please start another emulator.")

    return running_emulators
