'''A cron wrapper that tells you more about your cron jobs
'''

from __future__ import absolute_import
from __future__ import print_function

from .config import config
from .logger import logger


def main():
    print("Here is our logger: " + str(logger))
    print("Here is our config: " + str(config))


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


if __name__ == '__main__':
    main()
