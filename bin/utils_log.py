DEBUG = 'debug'
INFO = 'info'
WARN = 'warn'
ERROR = 'error'
log_levels = {None: 0, DEBUG: 0, INFO: 1, WARN: 2, ERROR: 3}
log_level = 0


def log(msg, _log_level=99):
    if log_level <= _log_level:
        print(msg)


def error(msg, error_prefix=True, exit_script=True):
    log(("ERROR: {}".format(msg) if error_prefix else msg), log_levels[ERROR])
    if exit_script:
        quit(1)


def warn(msg):
    log(msg, log_levels[WARN])


def info(msg):
    log(msg, log_levels[INFO])


def debug(msg):
    log(msg, log_levels[DEBUG])


def set_log_level(new_log_level):
    global log_level
    log_level = 0
    if new_log_level not in log_levels.keys():
        error("invalid log level: {}".format(new_log_level))
    log_level = log_levels[new_log_level]
