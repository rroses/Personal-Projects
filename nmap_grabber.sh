#!/bin/bash

printf "Enter the target IP: "
read ip_address

if [[ $ip_address =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
   printf "Acceptable IP Address. Running Port Scan...\n"
else
   printf "Unacceptable IP Address. Exiting\n"
   exit 1
fi

python3 scanner.py $ip_address

printf "\n"

printf "To banner grab ports, enter a port number. To attempt a SSH Brute Force, enter ssh: "
read usr_input

if [[$usr_input == "ssh"]]; then
   nmap -Pn -p 22 --script ssh_brute $ip_address
elif [[$usr_input =~ ^[0-9]]]; then
   nmap -Pn -p $usr_input -sV  --script=banner $ip_address
else
   printf "Incorrect Input. Exiting\n"
   exit 1
fi













