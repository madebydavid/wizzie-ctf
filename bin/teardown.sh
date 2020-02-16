#!/bin/bash

# Run this script to undo the permission settings

scriptDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

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

# make all files owned by current user
sudoFindRun "*.*" chown "$USER:$USER"

# reset perms on the flags
sudoFindRun "flag.txt" chmod 0664

# reset the perms on get-flag scripts
sudoFindRun "get-flag.py" chmod 0777

# Remove the suid python3
sudo rm "$scriptDir/python3"
