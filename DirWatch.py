#!/usr/bin/python2.7

import logging
import os
import sys
import getopt
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
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

class FileSystemWatcher(FileSystemEventHandler):

    def on_created(self, event):
        log.debug("File Created:" + event.src_path)

        publish.multiple([{"topic": "home/motion/diningMotion", "payload": "{0}", "qos": 0, "retain": False}], hostname="192.168.0.61", port="1883", client_id="DirWatcher", auth=None)

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
    observer = Observer()
    observer.schedule(FileSystemWatcher(), path)
    observer.start()
    #observer.schedule(directoryEventHandler, )

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

main(sys.argv[1:])