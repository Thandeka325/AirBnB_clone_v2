#!/usr/bin/python3
"""
Fabric scriptthat generates a .tgz archive from the contents
of the web_static folder.
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """

    time = datetime.now()
    archive_name = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive_name))
    if create is not None:
        return archive_name
    else:
        return None
