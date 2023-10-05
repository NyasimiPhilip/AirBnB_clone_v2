#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

sudo apt update -y
sudo apt upgrade -y
sudo apt install nginx -y

if [ ! -d /data/ ]; then
    mkdir -p /data/web_static/releases/test
fi


if [ ! -d /data/web_static/shared ]; then
    mkdir -p /data/web_static/shared
fi
cd /data/web_static/releases/test || exit
# create fake html file
touch index.html

echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > index.html

# check if sym link exists, delete it on every execution
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi

# create the symlink
ln -s /data/web_static/releases/test /data/web_static/current 

sudo chown -R ubuntu:ubuntu /data/
