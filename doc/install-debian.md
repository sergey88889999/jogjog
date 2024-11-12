# Cоздание виртуальной машины(VirtualBox) для тестового сервера: 

## Настройки виртуальной машины

Используемые параметры виртуальной машины:
- **Оперативная память**: 2 ГБ
- **Процессор**: 2 ядра
- **Диск**: 20 ГБ
- **Сетевые настройки**: сетевой мост
  
Система и настройки:
- **Система**: Debian 12.7
- **Локализация**: русский язык, местоположение — Германия
- **Предустановленные компоненты**: SSH-сервер и стандартные системные утилиты


### Установка программ

```bash
su
apt install sudo mc vim htop
```

### Настройка пользователя
Добавление пользователя в sudoers (по умолчанию не работает):

```bash
su
sudo usermod -aG sudo user123
```
### Настройка статического IP для доступа по SSH
Откройте файл /etc/network/interfaces:
```bash
sudo vim /etc/network/interfaces
```

Пример настройки:
```bash
auto eth0
iface eth0 inet static
		address 192.168.0.70
	netmask 255.255.255.0
		gateway 192.168.0.1
	dns-nameservers 8.8.8.8 8.8.4.4
```

отключил ipv6:

Откройте файл /etc/sysctl.conf
```bash
sudo vim /etc/sysctl.conf
```
изменяемые параметры:
```bash
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
```
далее: reboot

проверка сети:
```bash
ping google.com и 8.8.8.8
```

### Добавляем репозитории для обновления системы:
Откройте файл /etc/apt/sources.list
```bash
sudo vim /etc/apt/sources.list
```
Образец моих стандартых репозиториев:
```bash
deb   http://mirror.de.leaseweb.net/debian/ bookworm main non-free-firmware
deb-src http://mirror.de.leaseweb.net/debian/ bookworm main non-free-firmware
	
deb http://security.debian.org/debian-security bookworm-security main non-free-firmware
	
deb-src http://security.debian.org/debian-security bookworm-security main non-free-firmware
	
# bookworm-updates, to get updates before a point release is made;
# see https://www.debian.org/doc/manuals/debian-reference/ch02.en.html#_updates_and_backports
deb http://mirror.de.leaseweb.net/debian/ bookworm-updates main non-free-firmware
deb-src http://mirror.de.leaseweb.net/debian/ bookworm-updates main non-free-firmware

# This system was installed using small removable media
# (e.g. netinst, live or single CD). The matching "deb cdrom"
# entries were disabled at the end of the installation process.
# For information about how to configure apt package sources,
# see the sources.list(5) manual.
```

### Настройка ключа ssh

проверка, работает ли ssh-сервер:
```bash
sudo systemctl status ssh
```

#### Для доступа из под Windows10-11 используем putty:
скачать можно отсюда: https://www.putty.org/
##### добавляем ssh ключ:
генерируем ключи например в puttygen (RSA 2048)
сохраняем в jogjog.pub(пойдет на сервер)  и jogjog.ppk пойдет в putty
на сервере:
```bash
mkdir -p ~/.ssh
vim ~/.ssh/authorized_keys
```
ключ должен быть типа:
```bash
ssh-rsa AAAB3Nz … lBylB9jtXwjUokm  rsa-key-20241013
```

в одну строчку без лишних пробелов и доп символов, можно прямо из puttygen скопировать, там удобный формат в окне где будет показан сгенерированный ключ

выставляем права:
```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

ярлык для putty на рабочем столе(если нужно): 
```
"C:\Program Files\PuTTY\putty.exe" -load "jogjog"
```
можно вход по пользователю отключить, дополнительно настроить безопасность и файрволл но мы же тестовый сервер(!) разворачиваем

### установка Git:
```bash
sudo apt install git
```

### установка Docker: 
инструкция по установке Docker-a взята отсюда https://docs.docker.com/engine/install/debian/

#### удаляем старые пакеты есть вдруг есть:
```bash
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

#### добавляем репозиторий:
```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

устанавливаем из репозитория:
```bash 
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

проверяем работоспособность:
```bash
sudo docker run hello-world			cкачал контейнер и запустил	
sudo docker ps -a  				посмотреть ID остановленного контейнера
sudo docker rm 993				удалить этот контейнер (993- это начало его ID)
sudo docker images				посмотреть все скачанные образы контейнеров
sudo docker image rm hello-world 		ну и удалить его за ненадобностью
```

## можно для удобства сделать клон виртуальной машины:

клонирую виртуалку в командной строке Windows(Ctrl + R: cmd)
```bash
cd C:\Program Files\Oracle\VirtualBox
VBoxManage clonevm "jogjog" --name "jogjog-clone" --register
```
флаг –register добавляет склонированую машину в VirtualBox (опционально)

