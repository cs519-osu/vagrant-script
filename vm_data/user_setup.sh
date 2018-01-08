#!/bin/sh
cp /host_data/id_ecdsa* /home/ubuntu/.ssh
mkdir /home/ubuntu/bin
echo "export PATH=\$PATH:/home/ubuntu/bin" >> /home/ubuntu/.bashrc
cp /host_data/connect /home/ubuntu/bin
