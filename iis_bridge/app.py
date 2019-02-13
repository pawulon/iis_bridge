"""
    This module is used for manipulating iis applications
    :copyright: (c) 2014 by Kourosh Parsa.
"""

import iis_bridge.config as config


def exists(site_name, app_path):
    """ given the site name and app path, returns whether
    the application already exists
    Parameters:
    - site_name: name of iis site that contains the application
    - app_path: virtual path of the application, e.g. "/my_app"
    """
    full_app_path = site_name + app_path
    cmd = "%s list apps %s" % (config.APP_CMD, full_app_path)
    output = config.run(cmd)
    for line in output.splitlines():
        if line.split('"')[1] == full_app_path:
            return True
    return False


def create(site_name, app_path, physical_path=None):
    """ creates a new iis application
    Parameters:
    - site_name: name of iis site that will contain the application
    - app_path: virtual path of the application, e.g. "/my_app"
    - physical_path: the directory of the application
    """
    if exists(site_name, app_path):
        print("%s already exists in %s." % (app_path, site_name))
        return

    cmd = "%s add app /site.name:\"%s\" /path:\"%s\"" \
          % (config.APP_CMD, site_name, app_path)
    if physical_path:
        cmd += " /physicalPath:\"%s\"" % physical_path
    config.run(cmd)
