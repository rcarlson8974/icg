#!/usr/bin/env python

import os

from utils_log import *


def __exists(path, exit_if_not_found=True):
    exists = False
    parent_dir = os.path.abspath(os.path.join(path, os.pardir))
    if os.path.exists(parent_dir):
        for handle in os.listdir(parent_dir):
            real_path = os.path.join(parent_dir, handle)
            if os.path.exists(real_path) and os.path.abspath(path) == os.path.abspath(real_path):
                exists = True
                break

    if not exists:
        msg = "path does not exist: {}".format(path)
        if exit_if_not_found:
            error(msg)
        else:
            debug(msg)
            return None
    return path


def isdir(path, exit_if_not_found=True, create_dir=False):
    debug("checking if dir exists: {}".format(path))
    if not __exists(path=path, exit_if_not_found=False) and create_dir:
        os.makedirs(path)
    return __exists(path=path, exit_if_not_found=exit_if_not_found)


def isfile(path, exit_if_not_found=True):
    debug("checking if file exists: {}".format(path))
    return __exists(path=path, exit_if_not_found=exit_if_not_found)
