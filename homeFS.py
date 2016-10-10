#!/usr/bin/python2.7

import os
import logging
import sys
import getopt

log = None

def initLogger(name):
    global log
    logging.basicConfig(filename=os.path.normpath(os.path.dirname(os.path.realpath(__file__)) + "/" + name + ".log"), level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    log = logging.getLogger(__name__)
    soh = logging.StreamHandler(sys.stdout)
    soh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
    log.addHandler(soh)
    log.setLevel(logging.INFO)

def main(argv):
    2
    initLogger("renameandmove")

    try:
        opts, args = getopt.getopt(argv, "hr:", ["s=", "t=", "pre"])
    except getopt.GetoptError:
        print("MoveAndRename.py -h -r --s --t --pre")
        sys.exit(1)

    prefix = ""

    for opt, arg in opts:
        if opt in '-h':
            print("MoveAndRename.py -h -r --s --t --pre")
            sys.exit(2)
        elif (opt == "--s"):
            source = arg
        elif (opt == "--t"):
            target = arg
        elif (opt == "--pre"):
            prefix = arg

        os.path.basename(source)

    log.debug("Source = " + source + " Target = " + target)

main(sys.argv[1:])

