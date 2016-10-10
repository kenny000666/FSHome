import logging
import os
import sys
import getopt
import watchdog
import paho.mqtt.publish as publish

log = None
isMountedDirectory = False

def initLogger(name):
    global log
    logging.basicConfig(filename=os.path.normpath(os.path.dirname(os.path.realpath(__file__)) + "/" + name + ".log"), level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    log = logging.getLogger(__name__)
    soh = logging.StreamHandler(sys.stdout)
    soh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
    log.addHandler(soh)
    log.setLevel(logging.INFO)

def main(argv):
    initLogger("DirWatch")

    try:
        opts, args = getopt.getopt(argv, "hm:", ["t="])
    except getopt.GetoptError:
        print(__name__ + "-h --t")
        sys.exit(1)

    for opt, arg in opts:
        if opt in '-h':
            print(__name__ + "-h--t")
            sys.exit(2)
        elif opt == "-m":
            isMountedDirectory = True
        elif opt == "--t":
            target = arg




main(sys.argv[1:])