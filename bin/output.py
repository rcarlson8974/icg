#!/usr/bin/python3
import csv
import re
import shutil
import subprocess
import sys
from glob import glob
from optparse import OptionParser

from utils_log import *


class GenerateReport:

    def __init__(self, options):
        set_log_level(str(options.log_level).lower())

        with open("/Users/Z001MVB/Desktop/con.txt") as file:
            for item in file:
                item = item.strip()
                item = ' '.join(item.split())
                print(item)
                # print(item.strip())
                # print(item.strip())
                # print(item.strip())
                # print(item.strip())


def validate_usage(options):
    usage = "usage: {} [-d (--disable-dry-run)]".format(sys.argv[0])
    usage += "\nNote: optional flags [--ci] (indicates running in a CI build)"

    if bool(options.help):
        log(usage)
        quit(1)

    if options.log_level is None or str(options.log_level).lower() not in log_levels.keys():
        options.log_level = INFO

    return options

def main():
    parser = OptionParser(add_help_option=False)
    parser.add_option("--dry-run", action="store_true", dest="dry_run", default=False)
    parser.add_option("--log-level", dest="log_level", default=ERROR)
    parser.add_option("-h", "--help", action="store_true", dest="help", default=False)

    try:
        (options, args) = parser.parse_args()
    except:
        options = None

    set_log_level(ERROR)
    GenerateReport(validate_usage(options))


if __name__ == '__main__':
    main()
