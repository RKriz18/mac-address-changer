#!/usr/bin/env python3
"""
mac_changer.py

A simple command-line tool to change the MAC address of a network
interface on Linux, using ifconfig via subprocess.

Built as a hands-on Python + Linux networking project in a Kali Linux
home lab, as part of ongoing cybersecurity self-study.

Usage:
    sudo python3 mac_changer.py

You will be prompted for:
    Interface       e.g. eth0
    New MAC Address e.g. 00:11:22:33:44:55

Note: requires root privileges and the 'net-tools' package (for ifconfig).
"""

import subprocess


def change_mac(interface: str, mac_address: str) -> None:
    """Bring an interface down, set a new MAC address, then bring it back up."""
    print(f" [+] Changing MAC address for {interface} to {mac_address}")
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + mac_address, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)


def main():
    interface = input("Interface > ")
    mac_address = input("New MAC Address > ")
    change_mac(interface, mac_address)


if __name__ == "__main__":
    main()
