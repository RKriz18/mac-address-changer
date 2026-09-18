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

#!/usr/bin/env python3

import subprocess

# Ask the user which interface to target and what MAC address to set
interface = input("Interface > ")
mac_address = input("New MAC Address > ")

print(" [+] Changing MAC Address for " + interface + " to " + mac_address)

# Bring the interface down, apply the new MAC address, then bring it back up
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + mac_address, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
