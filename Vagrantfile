# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"
MEMORY = `sysctl -n hw.memsize`.to_i / 1024 / 1024 / 2
CPUS = `sysctl -n hw.ncpu`.to_i

FORWARD_PORTS = [5000,8000]

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.ssh.forward_agent = true

  FORWARD_PORTS.each do |port|
    config.vm.network :forwarded_port, host: port, guest: port
  end

  # add github to the list of known_hosts
  config.vm.provision :shell do |shell|
    shell.inline = "mkdir -p $1 && touch $2 && ssh-keyscan -H $3 >> $2 && chmod 600 $2"
    shell.args = %q{/root/.ssh /root/.ssh/known_hosts "github.com"}
  end

  if ENV['VM'] == "virtualbox"
      config.vm.box = "ubuntu/trusty32"
      config.vm.provider "virtualbox" do |v, override|
        v.memory = MEMORY
        v.cpus = CPUS
      end
  else
      config.vm.box = "parallels/ubuntu-14.04"
      config.vm.provider "parallels" do |v, override|
        v.update_guest_tools = true
        v.memory = MEMORY
        v.cpus = CPUS
      end
  end
end
