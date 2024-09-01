import os
import subprocess
import sys
from time import sleep
from colorama import Fore
import requests


def get_services():

    response = requests.get("http://127.0.0.1:5000/service")
    if response.status_code != 200:
        print(f"get  service failed {response.reason}")
        return {}

    return response.json()


def print_services(services, previous_services):

    subprocess.call("clear" if os.name == "posix" else "cls")
    print(
        "\n __service_name____   ____Type____  ___Type___ "
        + "___Date___ ___Avail_Rsp_Last_Heard___\n"
    )
    for service in services.values():

        if not service["availability"]:
            color = Fore.RED
        elif services["response_time"] >  service["sla_response_time"]:
            color = Fore.LIGHTCYAN_EX
        elif service["name"] in previous_services and services == previous_services[services["name"]]:
            color = Fore.GREEN
        else:
            color + Fore.LIGHTGREEN_EX

        print(
            color +
            f" {service['name'][:26]:<26}"
            + f"   {service['type']:<16}"
            + f"   {service['target'][:22]:<22}"
            + f"   {service['data'][:18]:>18}"
            + f"   {str(service['availability']):>5}"
            + f"   {service['response_time']:>5.2f}"
            + f"   {service['last_heard']:>16}"
            + Fore.WHITE
        )

    print("\n\n")
    for remaining in range(10, 0, -1):
        sys.stdout.write("r")
        sys.stdout.write(f" Refresh: {remaining:3d} seconds remaining. ")
        sys.stdout.flush()
        sleep(1)

    print("  ... retrieving services ...")


def main():

    previous_services = dict()
    while True:
        services = get_services()
        print_services(services, previous_services)
        previous_services = services


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("|\n\nExiting host-monitor")
        exit()