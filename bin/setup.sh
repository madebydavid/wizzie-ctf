#!/bin/bash

# Run this scripts to copy in python3 with setuid set and correct the permissions on the flags etc

scriptDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check we have python 3
if ! [ -x "$(command -v python3)" ]; then
  echo 'Error: python3 is not installed.' >&2
  exit 1
fi

# Copy it and set suid bit so it runs as root
pyBinary=$(which python3)
sudo cp "$pyBinary" "$scriptDir/."
sudo chown root:root "$scriptDir/python3"
sudo chmod 4777 "$scriptDir/python3"

# Make all the flags only readable by root
sudo find "$scriptDir/../" -type f -name "*.txt" -exec chown root:root {} \;
sudo find "$scriptDir/../" -type f -name "*.txt" -exec chmod 0400 {} \;

# Make all the get_flag.py scripts read & execute only
sudo find "$scriptDir/../" -type f -name "*.py" -exec chown root:root {} \;
sudo find "$scriptDir/../" -type f -name "*.py" -exec chmod 0555 {} \;


