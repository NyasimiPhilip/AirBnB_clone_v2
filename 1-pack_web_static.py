#!/usr/bin/python3
from datetime import datetime
from fabric.api import local
from time import strftime


def do_pack():
    """script that generates a .tgz archive from the
    contents of the web_static folder"""
    filedate = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filedate))
        # local(f"python -m tarfile -vc versions/{filedate} web_static/")
        return "versions/web_static_{}.tgz".format(filedate)
    except Exception as e:
        print(e)
        return None
