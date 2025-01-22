#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers.
"""

from fabric.api import env, local, put, run
from datetime import datetime
import os

# Define the IP addresses of the web servers
env.hosts = ['xx-web-01', 'xx-web-02']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: The path of the created archive, or None if the operation fails.
    """
    try:
        # Create the versions directory if it doesn't exist
        local("mkdir -p versions")

        # Generate the archive file name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f"versions/web_static_{timestamp}.tgz"

        # Create the archive
        local(f"tar -cvzf {archive_name} web_static")

        return archive_name
    except Exception as e:
        print(f"Error packing files: {e}")
        return None


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
        print(f"Error during deployment: {e}")
        return False


def deploy():
    """
    Creates and distributes an archive to web servers.

    Returns:
        bool: True if all operations are successful, otherwise False.
    """
    # Create the archive
    archive_path = do_pack()
    if archive_path is None:
        return False

    # Deploy the archive
    return do_deploy(archive_path)
