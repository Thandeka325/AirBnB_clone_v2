#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers.
"""
from fabric.api import env, put, run
import os

env.hosts = ['34.237.91.31', '18.234.169.141']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.

    Args:
        archive_path (str): The path to the archive file to be deployed.

    Returns:
        bool: True if all operations are successful, otherwise False.
    """
    if not os.path.isfile(archive_path):
        return False

    try:
        # Extract file name and base name without extension
        file_name = os.path.basename(archive_path)
        name_no_ext = file_name.split('.')[0]

        # Define the destination paths
        tmp_path = f"/tmp/{file_name}"
        release_path = f"/data/web_static/releases/{name_no_ext}/"

        # Upload the archive to the /tmp/ directory on the server
        if put(archive_path, tmp_path).failed:
            return False

        # Create the release directory
        if run(f"mkdir -p {release_path}").failed:
            return False

        # Uncompress the archive into the release directory
        if run(f"tar -xzf {tmp_path} -C {release_path}").failed:
            return False

        # Remove the archive from the server
        if run(f"rm {tmp_path}").failed:
            return False

        # Move content out of the web_static directory
        if run(f"mv {release_path}web_static/* {release_path}").failed:
            return False

        # Remove the now-empty web_static directory
        if run(f"rm -rf {release_path}web_static").failed:
            return False

        # Delete the current symbolic link
        if run("rm -rf /data/web_static/current").failed:
            return False

        # Create a new symbolic link
        if run(f"ln -s {release_path} /data/web_static/current").failed:
            return False

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Error during deployment: {e}")
        return False
