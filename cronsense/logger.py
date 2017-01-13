from __future__ import absolute_import
from __future__ import print_function

import logging
import logging.handlers
import os
import platform

def setup_logger():
    '''Enable logging to syslog and to file.

    Because we are a cron wrapper, it is IMPERATIVE that we do not log anything to stdout,
    otherwise cron will capture it and send it as an email.
    '''
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # TODO: only enable this in verbose/debugging mode?
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)

    if platform.system() == 'Linux':
        syslog_handler = logging.handlers.SysLogHandler(address='/dev/log')
    elif platform.system() == 'Darwin':
        # Darwin/macOS will ignore events lower than "error" level
        # Error level and higher get written to /var/log/system.log
        syslog_handler = logging.handlers.SysLogHandler(address='/var/run/syslog')
    else:
        syslog_handler = logging.handlers.SysLogHandler(address=('localhost', 514)) # Good luck!
    logger.addHandler(syslog_handler)

    return logger

logger = setup_logger()
