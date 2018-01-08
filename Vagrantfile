# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/xenial64"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder "./vm_data", "/host_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
     vb.memory = "2048"
     vb.cpus = 2
  end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", inline: <<-SHELL
    mv /etc/apt/sources.list /etc/apt/sources.list.save
    cp /host_data/sources.list /etc/apt/
    apt-get update
    apt-get install -y git python python-pip python-dev libssl-dev
    apt-get install -y libffi-dev build-essential python3 python3-pip
    apt-get install -y gcc-multilib gdb pandoc vim emacs wget curl binutils

    echo "PKG install DONE"

    pip install -U pip
    pip3 install -U pip
    pip install cryptography
    pip install pwntools
    echo "PIP install DONE"

    git clone https://github.com/cs519-osu/peda.git /home/ubuntu/peda
    echo "source ~/peda/peda.py" >> /home/ubuntu/.gdbinit
    echo "PEDA install DONE!"

    git clone --depth=1 https://github.com/amix/vimrc.git /home/ubuntu/.vim_runtime
    HOME=/home/ubuntu sh /home/ubuntu/.vim_runtime/install_awesome_vimrc.sh

    curl -R https://raw.githubusercontent.com/DenisCarriere/.bashrc/master/.bashrc >> /home/ubuntu/.bashrc
    echo >> /home/ubuntu/.vimrc; echo "set t_Co=256" >> /home/ubuntu/.vimrc

    sh /host_data/user_setup.sh

    chown -R ubuntu:ubuntu /home/ubuntu

  SHELL
end
