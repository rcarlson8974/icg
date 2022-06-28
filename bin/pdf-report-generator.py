#!/usr/bin/python3
import csv
import re
import shutil
import subprocess
import sys
from glob import glob
from optparse import OptionParser
from subprocess import Popen, PIPE

from utils_log import *


class GenerateReport:

    def __init__(self, options):
        set_log_level(str(options.log_level).lower())

        log("Generating PDF Report.........")
        log("")

        # Get the list of all files in the unprocessed dir
        unprocessed_pdfs = [val.split('/')[1] for val in glob('unprocessed/*.pdf')]
        for unprocessed_pdf in unprocessed_pdfs:
            log("Processing PDF {}".format(unprocessed_pdf))
            process_pdf(unprocessed_pdf)
            move_pdf(unprocessed_pdf)
            log("Done processing PDF {}".format(unprocessed_pdf))
            log("")
        log("Done Generating PDF Report.........")


def process_pdf(unprocessed_pdf):
    with open("reports/" + unprocessed_pdf + ".csv", 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Header info
        filewriter.writerow(["Project Name:", unprocessed_pdf])  # swap in real project name
        filewriter.writerow(["Customer:", "ACME Contracting"])  # swap in real customer name
        filewriter.writerow(["", ""])  # blank row
        filewriter.writerow(["", ""])  # blank row
        filewriter.writerow(["Key Words", "Page", "Count", "Sentence(s)"])

        # Swap in words you wanna search for here...
        materials = ["Quartz", "Granite", "Aluminum", "Concrete"]
        filewriter.writerow(["Materials"])
        for material in materials:
            result = grep_page_count(material, unprocessed_pdf)
            result.append(grep_sentence(material, unprocessed_pdf))
            filewriter.writerow(result)
        filewriter.writerow(["", ""])  # blank row after

        # Swap in competitors here...
        competitors = ["TMI", "Case Systems", "Leedo", "Saco", "Hansen Company", "ACG", "Wilkie", "Randawg Corp"]
        filewriter.writerow(["Competitors"])
        for competitor in competitors:
            result = grep_page_count(competitor, unprocessed_pdf)
            result.append(grep_sentence(competitor, unprocessed_pdf))
            filewriter.writerow(result)
        filewriter.writerow(["", ""])  # blank row after

        # Swap in characteristics here...
        characteristics = ["Face Frame", "PLAM", "Cabinet", "Countertop", "Casework", "Millwork", "Woodworking"]
        filewriter.writerow(["Characteristics"])
        for characteristic in characteristics:
            result = grep_page_count(characteristic, unprocessed_pdf)
            result.append(grep_sentence(characteristic, unprocessed_pdf))
            filewriter.writerow(result)


def grep_page_count(word, unprocessed_pdf):
    cmd = ['pdfgrep', '--ignore-case', '--cache', '--page-count', word, 'unprocessed/' + unprocessed_pdf]

    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, encoding='utf8')
        output = process.communicate()
        if ':' in format_grep(output):
            vals = format_grep(output).split(':')
            result = [word, vals[0], vals[1]]
        else:
            result = [word, "0", "0"]

        log("Page:Word Count for {} is {}".format(word, result))
        return result
    except subprocess.CalledProcessError as e:
        log("ERROR: {}", e.output)


def grep_sentence(word, unprocessed_pdf):
    cmd = ['pdfgrep', '--ignore-case', '--cache', word, 'unprocessed/' + unprocessed_pdf]
    grep_match = ".{0,0}" + word + ".{0,45}"

    try:

        pdfgrep_proc = Popen(cmd, stdout=PIPE, stderr=PIPE, encoding='utf8', universal_newlines=True)
        grep_proc = Popen(['grep', '-iEo', grep_match], stdin=pdfgrep_proc.stdout, stdout=PIPE, encoding='utf8')
        pdfgrep_proc.stdout.close()
        stdout, err = grep_proc.communicate()

        sentences = stdout
        log("Sentences for {} is {}".format(word, sentences))
        return sentences

    except subprocess.CalledProcessError as e:
        log("ERROR: {}", e.output)


def move_pdf(unprocessed_pdf):
    log("Moving PDF {} to processed folder".format(unprocessed_pdf))
    shutil.move("unprocessed/" + unprocessed_pdf, "processed/" + unprocessed_pdf)
    log("Done moving PDF {} to processed folder".format(unprocessed_pdf))


def format_grep(output):
    output = str(output)
    new_text = re.sub(r"[^a-zA-Z0-9:]", "", output)
    new_text = new_text.replace("nNone", "")
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
