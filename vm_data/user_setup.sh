#!/bin/sh
cp /host_data/id_ecdsa* /home/ubuntu/.ssh
chmod 400 /home/ubuntu/.ssh/id_ecdsa
mkdir /home/ubuntu/bin
echo "export PATH=\$PATH:/home/ubuntu/bin" >> /home/ubuntu/.bashrc
cp /host_data/connect /home/ubuntu/bin
