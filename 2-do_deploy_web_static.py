#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['34.237.91.31', '18.234.169.141']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False
    try:
        # Extract file name and name without extension
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        release_path = "/data/web_static/releases/"

        # Upload the archive to /tmp/
        put(archive_path, '/tmp/')
        # Create release directory
        run('mkdir -p {}{}/'.format(release_path, no_ext))
        # Uncompress the archive to the release directory
        run('tar -xzf /tmp/{} -C {}{}/'.format(
            file_name, release_path, no_ext))
        # Remove the uploaded archive
        run('rm /tmp/{}'.format(file_name))
        # Handle file structure: move files if needed
        run(
            'mv {0}{1}/web_static/* {0}{1}/ || true'.format(
                release_path, no_ext
            )
        )
        # Remove the now-empty `web_static` folder
        run('rm -rf {}{}/web_static'.format(release_path, no_ext))
        # Delete the old symbolic link and create a new one
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(
            release_path, no_ext))

        # Verify files exist in the correct location
        run('test -f /data/web_static/current/0-index.html')
