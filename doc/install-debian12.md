Cоздание виртуальной машины для  боевого сервера приложений debian 12.7

Я использовал такую:
    2 гига оперативки
	2 проца
	20 гигов диск
сетевые настройки: сетевой мост
локаль русская, месторасположение германия
ssh - сервер + стандартные системные утилиты

- установка программ:
su
apt install sudo mc vim htop

- В sudoers добавил пользователя своего, по автомату не работает, мне неудобно:
su
sudo usermod -aG sudo sergey13

- прописываем статический айпи для доступа по ssh:
sudo vim /etc/network/interfaces
	образец:
=================================
auto eth0
iface eth0 inet static
		address 192.168.0.70
	netmask 255.255.255.0
		gateway 192.168.0.1
	dns-nameservers 8.8.8.8 8.8.4.4
=========================

- отключил ipv6:
sudo vim /etc/sysctl.conf
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1

ребут и ping google.com и можно 8.8.8.8

- добавляем репозитории нормальные для обновления системы:
	sudo vim /etc/apt/sources.list
образец:
==========================
	#deb http://deb.debian.org/debian/ bookworm main
deb   http://mirror.de.leaseweb.net/debian/ bookworm main non-free-firmware
#deb-src http://deb.debian.org/debian/ bookworm main
deb-src http://mirror.de.leaseweb.net/debian/ bookworm main non-free-firmware
	
	
#deb http://security.debian.org/debian-security bookworm-security main
deb http://security.debian.org/debian-security bookworm-security main non-free-firmware
	
#deb-src http://security.debian.org/debian-security bookworm-security main
deb-src http://security.debian.org/debian-security bookworm-security main non-free-firmware
	
# bookworm-updates, to get updates before a point release is made;
# see https://www.debian.org/doc/manuals/debian-reference/ch02.en.html#_updates_and_backports
#deb http://deb.debian.org/debian/ bookworm-updates main
deb http://mirror.de.leaseweb.net/debian/ bookworm-updates main non-free-firmware
#deb-src http://deb.debian.org/debian/ bookworm-updates main
deb-src http://mirror.de.leaseweb.net/debian/ bookworm-updates main non-free-firmware

# This system was installed using small removable media
# (e.g. netinst, live or single CD). The matching "deb cdrom"
# entries were disabled at the end of the installation process.
# For information about how to configure apt package sources,
# see the sources.list(5) manual.
=================================
