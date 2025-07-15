import os
import platform
import subprocess

def print_system_uptime():
    """
    Prints the system uptime in a human-readable format.
    Supports Windows, Linux, and macOS.
    """
    system = platform.system()
    try:
        if system == "Windows":
            # Windows: Use 'net stats srv' or 'systeminfo'
            output = subprocess.check_output("net stats srv", shell=True, text=True, stderr=subprocess.DEVNULL)
            for line in output.splitlines():
                if "Statistics since" in line:
                    print(f"System uptime (Windows): {line}")
                    break
            else:
                print("Could not determine uptime on Windows.")
        elif system == "Linux":
            # Linux: Use /proc/uptime
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
                uptime_string = seconds_to_dhms(uptime_seconds)
                print(f"System uptime (Linux): {uptime_string}")
        elif system == "Darwin":
            # macOS: Use 'uptime' command
            output = subprocess.check_output("uptime", shell=True, text=True)
            print(f"System uptime (macOS): {output.strip()}")
        else:
            print(f"Unsupported OS: {system}")
    except Exception as e:
        print(f"Error retrieving uptime: {e}")

def seconds_to_dhms(seconds):
    days = int(seconds // 86400)
    hours = int((seconds % 86400) // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    parts = []
    if days > 0:
        parts.append(f"{days}d")
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0:
        parts.append(f"{minutes}m")
    parts.append(f"{secs}s")
    return ' '.join(parts)

if __name__ == "__main__":
    print_system_uptime()
