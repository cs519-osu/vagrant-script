#!/bin/bash
apt-get update
apt upgrade -y
apt-get install -y git python python-pip python-dev libssl-dev
apt-get install -y libffi-dev build-essential python3 python3-pip
apt-get install -y gcc-multilib gdb pandoc vim emacs wget curl binutils
echo "PKG install DONE"
