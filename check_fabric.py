from fabric import task

@task
def check_fabric():
    try:
        from fabric.api import local
        local("echo 'Fabric is working!'")
    except ImportError:
        print("Fabric is not properly installed.")

