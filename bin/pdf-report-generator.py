#!/usr/bin/python3
from optparse import OptionParser

from utils_file import *
from utils_log import *


class GenerateReport:

    def __init__(self, options):
        set_log_level(str(options.log_level).lower())
        log("Hello World")



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
    GenerateReport(options)


if __name__ == '__main__':
    main()
