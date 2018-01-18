#!/usr/bin/env python

import glob
import os

def remove_cr(fn):
    ran = False
    with open(fn, 'r+b') as f:
        data = f.read()
        data = "\n".join(data.split("\r\n"))
        f.seek(0)
        f.write(data)
        print("size %d" % len(data))
        f.truncate(len(data))
        f.close()
        ran = True
    return ran

def main():
    UN = 'ubuntu'
    if os.path.exists('/home/vagrant/.ssh'):
        UN = 'vagrant'

    os.system("git clone https://github.com/cs519-osu/peda.git /home/%s/peda" % UN)
    os.system('echo "source ~/peda/peda.py" >> /home/%s/.gdbinit' % UN)
    print("PEDA install DONE!")

    os.system("git clone --depth=1 https://github.com/amix/vimrc.git /home/%s/.vim_runtime" % UN)
    os.system("HOME=/home/%s sh /home/%s/.vim_runtime/install_awesome_vimrc.sh" % (UN, UN))

    os.system("curl -R https://raw.githubusercontent.com/DenisCarriere/.bashrc/master/.bashrc >> /home/%s/.bashrc" % UN)
    os.system('echo >> /home/%s/.vimrc; echo "set t_Co=256" >> /home/%s/.vimrc' % (UN, UN))




    os.system("cp /host_data/id_ecdsa* /home/%s/.ssh" % UN)
    os.system("chmod 400 /home/%s/.ssh/id_ecdsa" % UN)
    os.system("mkdir /home/%s/bin" % UN)
    os.system('echo "export PATH=\$PATH:/home/%s/bin" >> /home/%s/.bashrc' % (UN, UN))
    os.system("cp /host_data/connect /home/%s/bin" % UN)
    os.system("cp /host_data/fetch /home/%s/bin" % UN)

    files = glob.glob("/home/%s/bin/*" % UN)
    for fn in files:
        remove_cr(fn)

    os.system("chown -R %s:%s /home/%s" % (UN, UN, UN))

if __name__ == '__main__':
    main()
