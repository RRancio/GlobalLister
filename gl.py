import subprocess
import requests
import fade
import colorama
from colorama import Fore
import os

os.system("cls && title 'plugged usb detector - discord.gg/screenshare'")
os.system("mode con: cols=91 lines=30")
text = """
   _   ,--()
  ( )-'-.------|>
   "     `--[]
   plugged usb
    detector
"""

textl = fade.pinkred(text)

print(textl)

command = 'wmic path Win32_USBHub get DeviceID'
output = subprocess.check_output(command, shell=True)

filtered_output = [item for item in output.decode("utf-8").split("\n") if "VID_" in item or "PID_" in item]

vid_pid_values = [(item.split("VID_")[1].split("&")[0], item.split("PID_")[1].split("\\")[0]) for item in filtered_output]

for vid, pid in vid_pid_values:
    try:
        url = f"https://devicehunt.com/view/type/usb/vendor/{vid}/device/{pid}"
        response = requests.get(url, timeout=5)
        content = response.content.decode("utf-8")
        device_line = content.split('class="details --type-device --auto-link"><h3 class=\'details__heading\'>')[1].split("</h3><table")[0]
        vendor_line = content.split('class="details --type-vendor --auto-link"><h3 class=\'details__heading\'>')[1].split("</h3><table")[0]
        print(Fore.GREEN + "[+]" + Fore.WHITE + f" Detected {vid} + {pid} as: {device_line.strip()} - {vendor_line.strip()}\n")
    except requests.exceptions.Timeout:
        print(Fore.RED + "[!]" + Fore.WHITE + f" Unable to get {vid} + {pid} device.\n")
    except:
        print(Fore.RED + "[!]" + Fore.WHITE + f" Unable to get {vid} + {pid} device.\n")

os.system("pause")
