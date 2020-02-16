#!/bin/bash

# Run this script to copy in python3 with setuid set and correct the
# permissions on the flags etc

scriptDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check we have python 3
if ! [ -x "$(command -v python3)" ]; then
  echo 'Error: python3 is not installed.' >&2
  exit 1
fi

# -------------------------------------
# Run a given command sudo'd on a given file match in the lesson dirs
# Arguments:
#   nameMatch
#   command
# -------------------------------------
function sudoFindRun {
  nameMatch="$1"
  command="${@:2}"
  sudo find "$scriptDir/../" \
    -type f \
    -name "$nameMatch" \
    -path "*/lesson-*" \
    -exec $command {} \;
}

# Copy it and set suid bit so it runs as root
sudo cp $(which python3) "$scriptDir/python3"
sudo chown root:root "$scriptDir/python3"
sudo chmod 4777 "$scriptDir/python3"

# make all files owned by root
sudoFindRun "*.*" chown root:root

# make all flags readable only by root
sudoFindRun "flag.txt"  chmod 0400

# make all get-flag.py files read and execute only
sudoFindRun "get-flag.py" chmod 0555
