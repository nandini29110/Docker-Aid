#!/bin/bash
mkdir  /dvd
mount  /dev/cdrom    /dvd
echo "mount /dev/cdrom /dvd" >> /etc/rc.d/rc.local
chmod +x /etc/rc.d/rc.local
cp dvd.repo /etc/yum.repos.d/dvd.repo
dnf makecache
dnf install docker-ce --nobest  -y
firewall-cmd --zone=public --add-masquerade --permanent
firewall-cmd --zone=public --add-port=80/tcp --permanent
firewall-cmd --zone=public --add-port=443/tcp --permanent
firewall-cmd --reload
systemctl restart docker.service
systemctl enable  docker.service
docker pull centos:latest
docker pull ubuntu:latest
cp   {file}.py      /var/www/cgi-bin/{file}.py
chmod +x /var/www/cgi-bin/{file}.py