#!/usr/bin/python3
from fabric.api import local, env, put, run
from fabric import *
from time import strftime
import os


def do_pack():
    """script that generates a .tgz archive from the
    contents of the web_static folder"""

    filedate = strftime("%Y%m%d%H%M%S")
    try:
        if not os.path.exists('versions'):
            local("mkdir versions")

        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filedate))
        # local(f"python -m tarfile -vc versions/{filedate} web_static/")
        return "versions/web_static_{}.tgz".format(filedate)

    except Exception as e:
        return None


env.hosts = ['100.25.111.120', '54.152.132.135']
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


def do_deploy(archive_path):
    """script that distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False

    archive_path_extension = archive_path[-18:-4]
    try:
        put(archive_path, '/tmp')

        run('sudo mkdir -p /data/web_static/releases/web_static_{}'.
            format(archive_path_extension))

        # exctract the tgz contents
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C\
             /data/web_static/releases/web_static_{}'.
            format(archive_path_extension, archive_path_extension))

        # remove the archive
        run('sudo rm /tmp/web_static_{}.tgz'.format(archive_path_extension))

        # unpack the files
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
            /data/web_static/releases/web_static_{}'.
            format(archive_path_extension, archive_path_extension))

        run('sudo rm -rf /data/web_static/releases/web_static_{}/web_static'.
            format(archive_path_extension))

        # delete this symbolic link
        run('sudo rm -rf /data/web_static/current')
        # create new sym link
        run('sudo ln -s /data/web_static/releases/web_static_{}\
             /data/web_static/current'.format(archive_path_extension))
        return True
    except Exception as e:
        return False


def deploy():
    """script that creates and distributes
    an archive to my werb servers"""

    archive_path = do_pack()
    if not os.path.exists(archive_path):
        return False

    return do_deploy(archive_path)
