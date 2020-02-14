#!/bin/bash

# Run this script to undo the permission settings

scriptDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

sudo find "$scriptDir/../" -type f -name "*.txt" -exec chown "$USER:$USER" {} \;
sudo find "$scriptDir/../" -type f -name "*.txt" -exec chmod 0664 {} \;

sudo find "$scriptDir/../" -type f -name "*.py" -exec chown "$USER:$USER" {} \;
sudo find "$scriptDir/../" -type f -name "*.py" -exec chmod 0777 {} \;


