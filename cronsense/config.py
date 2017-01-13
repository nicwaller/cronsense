'''Prepare the configurations.

Opinion: Do away with command line options and arguments. They make the cron job look messy and confusing.
Use only namespaced environment variables and/or config files.
'''

# TODO: if profiling is enabled on any of the outputs, then cronsense will stay alive until the command finishes running.
# otherwise, it will dispatch the command asynchronously.
# but... what about stdout/stderr? We definitely want to stick around to receive those. So we will *always* be profiling.

from __future__ import absolute_import
from __future__ import print_function

import os
import yaml
import socket

# TODO: is it better to run the process myself, or set myself up as a pipe target


def find_config_file():
    '''Find the best config file.

    I guess the more pythonic approach would be to just try reading each file and then bail out with
    an exception. (Easier to Ask Forgiveness than Permission). But, here we are.
    '''

    config_file_precedence = [
        'cronsense.yaml',
        '.cronsense.yaml',
        os.path.expanduser('~/.cronsense.yaml'),
        '/etc/cronsense.yaml',
    ]
    for path in config_file_precedence:
        if os.path.exists(path):
            return path
    return None


def populate_config():
    default_config = {
        'cronsense': {
            'watch_stderr': True,
            'watch_exit': True,
        },
        'statsd': {
            'host': '127.0.0.1',
            'port': 8125,
            'prefix': 'cronsense',
        },
        'graphite': {
            'host': None,
            'line_port': 2003,
            'prefix': 'cronsense.' + socket.gethostname(),
        },
        'logstash': {
            'json_schema': 0,
            'logfile': '/var/log/cronsense-logstash.log',
            'include_envvars': True,
        }
    }

    # TODO: should i log using a watched file handler and risk breaking compatibility with logrotate?
    # Or should i log using a regular file handler and risk filling up the system?

    # TODO: use graphite line or pickle protocol? after all, we are in python...

    try:
        config_file = find_config_file()
        with open(config_file, 'r') as stream:
            config = yaml.load(stream)
    except Exception as e:
        print("whoa, got an exception")
        print(e)
    # TODO: package an example cronsense.yaml, or put it in ReadTheDocs or something

    statsd:
        host: 127.0.0.1
        port: 8125
        prefix: cronsense
    graphite:
        host: graphite.example.com
        port: 2003
        prefix: system.myhost1.cronsense
    logstash:
        json_schema: 0
        file:

    config_from_environment = {
        'statsd': {
            'host': os.environ.get('CRONSENSE_STATSD_HOST')
        }
    }

    config = {} # TODO: merge default, environment, and file based config with precedence
    # TODO: write a log entry when selecting one (or more) config files
    # TODO: write a log entry showing all the environment variables that were used


    environment_configvar_map = {
        'CRONSENSE_STATSD_HOST': 'statsd.host'
    }

    return config

    # TODO: definitely load the name of this job from environment variable
    # otherwise I guess it gets sent to statsd as an anonymous event
    # or... cronsense will try to guess it based on the daemon being executed

    # TODO: also support a config file, either specified or in a well-known location (~/.cronsense.rc or working directory)
    # TODO: what if statsd is running on a non-standard port?
    # try:
    # use_statsd = args.statsd or os.environ.get('CRONSENSE_STATSD') or True
    # use_graphite = args.graphite or os.environ.get('CRONSENSE_GRAPHITE') or False
    # logfile = args.logfile or os.environ.get('CRONSENSE_LOGFILE') or False


config = populate_config()




    # parser = argparse.ArgumentParser(description='Tells you more about your cron jobs')
    # parser.add_argument('-s', '--statsd', required=False, help='Send metrics to statsd')
    # parser.add_argument('-g', '--graphite', required=False, help='Send metrics directly to Graphite')
    # parser.add_argument('-f', '--logfile', required=False, help='Write to a logfile')
    # parser.add_argument('-l', '--logformat', required=False, help='What kind of logformat you like')
    # # TODO: somehow clearly distinguish between the cronsense logs vs.
    # # how logs of the child process will be directed

    # # TODO: logstash version 1 and version 0
    # # TODO: what if logrotate moves the file out from underneath us
    # # maybe later I will relent and add email options?
    # args = parser.parse_args()

    # print(args)
