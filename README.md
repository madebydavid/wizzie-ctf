# Wizzie Wizzie CTF

### This is a small set of security challenges. The goal of each is to get the contents of the `flag.txt` file

## Setup

Prerequisites:
- A machine running Linux
- Ability to run `sudo`
- Python3

We have to preconfigure things a little - we need a python binary which has root execute permissions and we need to lock down all the `flag.txt` files so that normal users cannot read them.

To get things setup:

```bash
git clone git@github.com:madebydavid/wizzie-ctf.git
cd wizzie-ctf
./bin/setup.sh
```

The `setup.sh` script will ask you to sudo - don't be alarmed when it prompts for a password.

There is a `teardown.sh` script which unsets the permissions on the files - this is useful when developing.

