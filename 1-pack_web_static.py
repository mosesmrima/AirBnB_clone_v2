#!/usr/bin/python3
# compress

import os.path
from datetiem import datetime
from fabric.api import local

def do_pack():
    """ This functions create a tar archive for the web_static directory """
    dt = datetime.utcnow()
    path = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
        if local("tar -cvzf {} web_static".format(path)).failed is True:
            return None
        return path
