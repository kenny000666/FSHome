#!/usr/bin/python2.7

import logging
import os
import sys
import getopt
from watchdog.observers import Observer
from watchdog.events import FileCreatedEvent
import paho.mqtt.publish as publish

log = None

def initLogger(name):
    global log
    logging.basicConfig(filename=os.path.normpath(os.path.dirname(os.path.realpath(__file__)) + "/" + name + ".log"), level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    log = logging.getLogger(__name__)
    soh = logging.StreamHandler(sys.stdout)
    soh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
    log.addHandler(soh)
    log.setLevel(logging.DEBUG)

def main(argv):
    initLogger("DirWatch")

    isMountedDirectory = False

    try:
        opts, args = getopt.getopt(argv, "h:m", ["Path="])
    except getopt.GetoptError:
        print(__name__ + "-h -m --Path")
        sys.exit(1)

    for opt, arg in opts:
        log.debug("Arguement: " + opt + " " + arg)
        if opt in '-h':
            print(__name__ + "-h -m --Path")
            sys.exit(2)
        elif opt == "-m":
            isMountedDirectory = True
        elif opt == "--Path":
            path = arg

    log.debug("Watch Directory: " + path)
    log.debug("Is Mounted Directory: " + str(isMountedDirectory))

    if isMountedDirectory:
        if os.path.ismount(path):
            log.debug("Path is mounted")
        else:
            log.debug("Path is not mounted")

    #directoryEventHandler = FileCreatedEvent()
    #observer = Observer()
    #observer.schedule(directoryEventHandler, )



main(sys.argv[1:])