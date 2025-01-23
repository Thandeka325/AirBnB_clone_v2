#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers.
"""

from fabric.api import put, run, env
import os

env.hosts = ['34.237.91.31', '18.234.169.141']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.

    Args:
        archive_path (str): Path to the archive file.

    Returns:
        bool: True if deployment was successful, False otherwise.
    """
    if not os.path.isfile(archive_path):
        print("Archive path does not exist.")
        return False

    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        release_path = f"/data/web_static/releases/{no_ext}/"

        # Upload the archive to /tmp/
        if put(archive_path, f"/tmp/{file_name}").failed:
            print("Failed to upload archive.")
            return False

        # Create the release directory
        if run(f"rm -rf {release_path}").failed or
        run(f"mkdir -p {release_path}").failed:
            print("Failed to create release directory.")
            return False

        # Uncompress the archive to the release directory
        if run(f"tar -xzf /tmp/{file_name} -C {release_path}").failed:
            print("Failed to uncompress archive.")
            return False

        # Remove the uploaded archive
        if run(f"rm /tmp/{file_name}").failed:
            print("Failed to remove archive from /tmp.")
            return False

        # Move files out of the `web_static` folder
        if run(f"mv {release_path}web_static/* {release_path}").failed:
            print("Failed to move files.")
            return False

        # Remove the now-empty `web_static` folder
        if run(f"rm -rf {release_path}web_static").failed:
            print("Failed to remove web_static directory.")
            return False

        # Delete the old symbolic link and create a new one
        if run("rm -rf /data/web_static/current").failed:
            print("Failed to remove old symbolic link.")
            return False
        if run(f"ln -s {release_path} /data/web_static/current").failed:
            print("Failed to create symbolic link.")
            return False

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
