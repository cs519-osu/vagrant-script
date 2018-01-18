#!/usr/bin/env python

import glob
import os
import subprocess


def get_username():
    result = subprocess.check_output("whoami", shell=True)
    return result.strip()

def get_homedir():
    result = subprocess.check_output("echo $HOME", shell=True)
    return result.strip()

def main():
    HD = get_homedir()
    UN = get_username()
    print("Username: %s Homedir %s" % (UN, HD))
    quit();
    os.system("git clone https://github.com/cs519-osu/peda.git %s/peda" % HD)
    os.system('echo "source ~/peda/peda.py" >> %s/.gdbinit' % HD)
    print("PEDA install DONE!")

    os.system("git clone --depth=1 https://github.com/amix/vimrc.git %s/.vim_runtime" % HD)
    os.system("HOME=%s sh %s/.vim_runtime/install_awesome_vimrc.sh" % (HD, HD))

    os.system("curl -R https://raw.githubusercontent.com/DenisCarriere/.bashrc/master/.bashrc >> %s/.bashrc" % HD)
    os.system('echo >> %s/.vimrc; echo "set t_Co=256" >> %s/.vimrc' % (HD, HD))

    os.system("mv %s/.ssh/id_ecdsa %s/.ssh/id_ecdsa.bak" % (HD, HD))
    os.system("cp vm_data/id_ecdsa %s/.ssh" % HD)
    os.system("chmod 400 %s/.ssh/id_ecdsa" % HD)
    os.system("mkdir %s/bin" % HD)
    os.system('echo "export PATH=\$PATH:%s/bin" >> %s/.bashrc' % (HD, HD))
    os.system("cp vm_data/connect %s/bin" % HD)
    os.system("cp vm_data/fetch %s/bin" % HD)

if __name__ == '__main__':
    main()
