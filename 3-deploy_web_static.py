#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to the web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = ['34.237.91.31', '18.234.169.141']


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        return None


def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        release_path = "/data/web_static/releases/"

        # Upload the archive to /tmp/
        put(archive_path, '/tmp/')
        # Create release directory
        run('mkdir -p {}{}/'.format(release_path, no_ext))
        # Extract archive contents
        run(
            'tar -xzf /tmp/{} -C {}{}/'.format(
                file_name, release_path, no_ext
            )
        )
        # Remove uploaded archive
        run('rm /tmp/{}'.format(file_name))
        # Move files from `web_static` directory
        run(
            'mv {0}{1}/web_static/* {0}{1}/ || true'.format(
                release_path, no_ext
            )
        )
        # Remove now-empty `web_static` directory
        run('rm -rf {}{}/web_static'.format(release_path, no_ext))
        # Update symbolic link
        run(
            'ln -s {}{}/ /data/web_static/current'.format(
                release_path, no_ext
            )
        )

        # Validate deployment
        run('test -f /data/web_static/current/my_index.html')
        return True
    except Exception as e:
        print(f"Deployment error: {e}")
        return False


def deploy():
    """Creates and distributes an archive to the web servers."""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
