#!/usr/bin/python3
from datetime import datetime
from invoke import task
from invoke import Connection
from time import strftime

@task
def pack(c):  # Accept a Context argument 'c'
    result = do_pack()
    if result:
        print(f"File created: {result}")
    else:
        print("Packaging failed.")

def do_pack():
    """script that generates .tgz archive from the
    contents of the web_static folder"""

    filedate = strftime("%Y%m%d%H%M%S")
    try:
        c = Connection('localhost')  # Create a connection to the local host
        c.local("mkdir -p versions")
        c.local("tar -czvf versions/web_static_{}.tgz web_static/"
                .format(filedate))
        return "versions/web_static_{}.tgz".format(filedate)

    except Exception as e:
        print(e)
        return None

