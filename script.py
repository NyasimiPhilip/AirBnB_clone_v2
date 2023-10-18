from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Create a .tgz archive of the web_static folder
    """
    try:
        # Get the current date and time
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")

        # Create the "versions" directory if it doesn't exist
        local("mkdir -p versions")

        # Archive the web_static folder
        archive_name = "web_static_{}.tgz".format(timestamp)
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the archive path if successful
        return "versions/{}".format(archive_name)
    except Exception:
        return None

if __name__ == "__main__":
    result = do_pack()
    if result is not None:
        print("Web static packed: {}".format(result))
    else:
        print("Pack failed")

