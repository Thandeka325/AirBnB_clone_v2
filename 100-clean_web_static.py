#!/usr/bin/python3
"""
Fabric script to delete out of date archives.
"""

import os
from fabric.api import *

env.hosts = ['34.237.91.31', '18.234.169.141']


def do_clean(number=0):
    """Delete out-of-date archives in the local and remote servers.

    Args:
        number (int): The number of the most recent archives to keep.
                      If number is 0 or 1, keep only the most recent.
                      If number is 2, keep the most recent and,
                      second most recent, etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
