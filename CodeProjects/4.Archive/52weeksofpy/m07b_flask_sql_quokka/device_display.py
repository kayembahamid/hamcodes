import os
import subprocess
import sys
from time import sleep
from colorama import Fore

import requests


DISPLAY_WAIT_TIME = 10


def get_devices():

    response = requests.get("http://127.0.0.1:5001/devices")
    if response.status_code != 200:
        print(f"get device failed: {response.reason}")
        return {}

    return response.json()


def print_devices(devices, previous_devices):

    subprocess.call("clear" if os.name == "posix" else "cls")
    print(
        "\n  __Device_Name________  ___IP_address___ _____Model______"
        +"_Version_ _Avail_ __Rsp__ ___Last_Heard_______\n"
    )
    for device in devices.values():

        if not device["availability"]:
            color = Fore.RED
        elif device["name"] in previous_devices and device == previous_devices[device["name"]]:
            color = Fore.GREEN
        else:
            color = Fore.LIGHTGREEN_EX

        print(
            color +
            f"  {device['hostname'][:26]:<24}"
            + f"   {device['ip_address']:<16}"
            + f"   {device['model'][:16]:<16}"
            + f"   {device['os_version']:>}"
            + f"   {str(device['availbility']):>5}"
            + f"   {device['response_time']:>5.2f}"
            + f"   {device['last_heard']:>5.2f}"
            + Fore.WHITE
        )

    print("\n\n")
    for remaining in range(DISPLAY_WAIT_TIME, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(f" Refresh: {remaining:3d} seconds remaining.")
        sys.stdout.flush()
        sleep(1)

    print("   .... retrieving device ...")


def main():

    previous_devices = dict()
    while True:
        devices = get_devices()
        print_devices(devices, previous_devices)
        previous_devices = devices

