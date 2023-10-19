#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers using the function do_deploy.
"""

from fabric.api import env, put, run
import os

# Replace with your actual server IP addresses
env.hosts = ['54.146.71.185', '54.144.138.139']

# Replace with your actual SSH user and key path
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_deploy(archive_path):
    """Distribute an archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/
        put(archive_path, '/tmp/')

        # Extract the archive filename without extension
        archive_filename = os.path.basename(archive_path)
        archive_name = archive_filename.split('.')[0]

        # Create the release directory
        run('sudo mkdir -p /data/web_static/releases/{}'.format(archive_name))

        # Uncompress the archive
        run('sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}'.
            format(archive_filename, archive_name))

        # Remove the archive from /tmp/
        run('sudo rm /tmp/{}'.format(archive_filename))

        # Delete the symbolic link /data/web_static/current
        run('sudo rm -f /data/web_static/current')

        # Create a new symbolic link
        run('sudo ln -s /data/web_static/releases/{} /data/web_static/current'.
            format(archive_name))

        return True

    except Exception as e:
        return False

