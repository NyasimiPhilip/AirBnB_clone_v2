#!/usr/bin/python3
from fabric.api import env, put, run
import os

# Replace with your actual server IP addresses
env.hosts = ['54.146.71.185', '54.144.138.139']

# Replace with your actual SSH user and key path
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_deploy(archive_path):
    """Script that distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False

    archive_path_extension = archive_path[-18:-4]
    try:
        put(archive_path, '/tmp')

        run('sudo mkdir -p /data/web_static/releases/web_static_{}'.
            format(archive_path_extension))

        # Extract the tgz contents
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C\
             /data/web_static/releases/web_static_{}'.
            format(archive_path_extension, archive_path_extension))

        # Remove the archive
        run('sudo rm /tmp/web_static_{}.tgz'.format(archive_path_extension))

        # Unpack the files
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
            /data/web_static/releases/web_static_{}'.
            format(archive_path_extension, archive_path_extension))

        run('sudo rm -rf /data/web_static/releases/web_static_{}/web_static'.
            format(archive_path_extension))

        # Delete the symbolic link
        run('sudo rm -rf /data/web_static/current')
        # Create a new symbolic link
        run('sudo ln -s /data/web_static/releases/web_static_{}\
             /data/web_static/current'.format(archive_path_extension))
        return True
    except Exception as e:
        return False

