#!/usr/bin/python3
import csv
import re
import subprocess
import sys
from glob import glob
from optparse import OptionParser

from utils_log import *


class GenerateReport:

    def __init__(self, options):
        set_log_level(str(options.log_level).lower())

        log("Generating PDF Report.........")

        # Get the list of all files in the unprocessed dir
        unprocessed_pdfs = [val.split('/')[1] for val in glob('unprocessed/*.pdf')]
        for unprocessed_pdf in unprocessed_pdfs:
            log("Unprocessed PDF {}".format(unprocessed_pdf))
            process_pdf(unprocessed_pdf)
            log("")
        log("Done Generating PDF Report.........")


def process_pdf(unprocessed_pdf):
    with open("reports/" + unprocessed_pdf + ".csv", 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        # Header info
        filewriter.writerow(["Project Name:", "Sample Project"])  # swap in real project name
        filewriter.writerow(["Customer:", "ACME Contracting"])  # swap in real customer name
        filewriter.writerow(["", ""])  # blank row
        filewriter.writerow(["", ""])  # blank row
        filewriter.writerow(["Key Words", "Page", "Count"])
        filewriter.writerow(["Materials"])

        # Swap in words you wanna search for here...
        search_words = ["Quartz", "Granite", "Aluminum", "Concrete"]
        grep_words(filewriter, search_words, unprocessed_pdf)
        filewriter.writerow(["", ""])  # blank row after

        # Swap in competitors here...
        competitors = ["TMI", "Case Systems", "Leedo", "Saco", "Hansen Company", "ACG", "Wilkie", "Randawg Corp"]
        filewriter.writerow(["Competitors"])
        grep_words(filewriter, competitors, unprocessed_pdf)
        filewriter.writerow(["", ""])  # blank row after

        # Swap in characteristics here...
        characteristics = ["Face Frame", "PLAM", "Cabinet", "Countertop", "Casework", "Millwork", "Woodworking"]
        filewriter.writerow(["Characteristics"])
        grep_words(filewriter, characteristics, unprocessed_pdf)


def grep_words(filewriter, words, unprocessed_pdf):
    for word in words:
        cmd = ['pdfgrep', '--ignore-case', '--page-count', word, 'unprocessed/' + unprocessed_pdf]

        try:
            output = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            output = output.communicate()
            log("Page:Word Count for {} is {}".format(word, format_grep(output)))

            if ':' in format_grep(output):
                vals = format_grep(output).split(':')
                filewriter.writerow([word, vals[0], vals[1]])
            else:
                filewriter.writerow([word, "0", "0"])

        except subprocess.CalledProcessError as e:
            log("ERROR: {}", e.output)


def format_grep(output):
    output = str(output)
    new_text = re.sub(r"[^a-zA-Z0-9:]", "", output)
    new_text = new_text.replace("b", "")
    new_text = new_text.replace("n", "")
    new_text = new_text.replace("|", "")
    new_text = new_text.replace("Noe", "")
    # new_text = new_text.replace(":", ",")
    new_text = new_text.strip()
    return new_text


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
