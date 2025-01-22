#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives.
"""

import os
from fabric.api import env, run, local

env.hosts = ["34.237.91.31", "18.234.169.141"]


def do_clean(number=0):
    """
    Deletes out-of-date archives in the local and remote servers.

    Args:
        number (int): The number of the most recent archives to keep.
                      If number is 0 or 1, keep only the most recent.
                      If number is 2, keep the most recent and,
                      second most recent, etc.
    """
    # Get list of archives in the local versions directory
    local_archives = sorted(local("ls -t versions", capture=True).splitlines())

    # If the number is 0 or 1, keep only the most recent archive
    if number == 0 or number == 1:
        archives_to_keep = 1
    else:
        archives_to_keep = number

    # Remove the archives in the local 'versions' folder.
    if len(local_archives) > archives_to_keep:
        for archive in local_archives[archives_to_keep:]:
            local(f"rm versions/{archive}")

    # Get list of archives in the remote server's releases folder
    for host in env.hosts:
        remote_archives = run("ls -t /data/web_static/releases").splitlines()

        # Remove the archives in the remote releases folder.
        if len(remote_archives) > archives_to_keep:
            for archive in remote_archives[archives_to_keep:]:
                run(f"rm -rf /data/web_static/releases/{archive}")
