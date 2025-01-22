#!/usr/bin/python3
"""
Fabric script distribute an archive to web servers.
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
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract file name and base name without extension
        file_name = os.path.basename(archive_path)
        file_no_ext = file_name.split('.')[0]

        # Define the destination paths
        tmp_path = f"/tmp/{file_name}"
        release_path = f"/data/web_static/releases/{file_no_ext}/"

        # Upload the archive to the /tmp/ directory on the server
        put(archive_path, tmp_path)

        # Create the release directory
        run(f"mkdir -p {release_path}")

        # Uncompress the archive into the release directory
        run(f"tar -xzf {tmp_path} -C {release_path}")

        # Remove the archive from the server
        run(f"rm {tmp_path}")

        # Move content out of the web_static directory
        run(f"mv {release_path}web_static/* {release_path}")

        # Remove the now-empty web_static directory
        run(f"rm -rf {release_path}web_static")

        # Delete the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run(f"ln -s {release_path} /data/web_static/current")

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
