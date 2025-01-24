#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to the web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = ['34.237.91.31', '18.234.169.141']


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        release_path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(release_path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(
            file_name, release_path, no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(release_path, no_ext))
        run('rm -rf {}{}/web_static'.format(release_path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(
            release_path, no_ext))
        return True
    except Exception as e:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
