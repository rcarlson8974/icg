#!/usr/bin/python3
from optparse import OptionParser

import sys
import subprocess

from utils_file import *
from utils_log import *


class GenerateReport:

    def __init__(self, options):
        set_log_level(str(options.log_level).lower())

        log("Generating PDF Report.........")

        # Swap in words you wanna search for here...
        search_words = ["Allowable", "Taxes", "Steel"]

        for search_word in search_words:
            ps = subprocess.Popen(('pdfgrep', search_word, 'unprocessed/Receipt.pdf'), stdout=subprocess.PIPE)
            output = subprocess.check_output(('wc', '-l'), stdin=ps.stdout)
            log("Word Count for {} is {}".format(search_word, output))
            ps.wait()

        log("Done Generating PDF Report.........")

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
