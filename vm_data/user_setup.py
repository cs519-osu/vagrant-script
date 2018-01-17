#!/usr/bin/env python

import os

git clone https://github.com/cs519-osu/peda.git /home/ubuntu/peda
echo "source ~/peda/peda.py" >> /home/ubuntu/.gdbinit
echo "PEDA install DONE!"

git clone --depth=1 https://github.com/amix/vimrc.git /home/ubuntu/.vim_runtime
HOME=/home/ubuntu sh /home/ubuntu/.vim_runtime/install_awesome_vimrc.sh

curl -R https://raw.githubusercontent.com/DenisCarriere/.bashrc/master/.bashrc >> /home/ubuntu/.bashrc
echo >> /home/ubuntu/.vimrc; echo "set t_Co=256" >> /home/ubuntu/.vimrc


chown -R ubuntu:ubuntu /home/ubuntu


cp /host_data/id_ecdsa* /home/ubuntu/.ssh
chmod 400 /home/ubuntu/.ssh/id_ecdsa
mkdir /home/ubuntu/bin
echo "export PATH=\$PATH:/home/ubuntu/bin" >> /home/ubuntu/.bashrc
cp /host_data/connect /home/ubuntu/bin
cp /host_data/fetch /home/ubuntu/bin
