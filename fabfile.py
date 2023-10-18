from fabric.api import task, local
from _1_pack_web_static import do_pack  # Import the do_pack function from your script

@task
def pack():
    result = do_pack()
    if result:
        print(f"File created: {result}")
    else:
        print("Packaging failed.")

