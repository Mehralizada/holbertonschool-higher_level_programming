#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)
    
    if argc == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argc, "s" if argc > 1 else ""))
        for i in range(argc):
            print("{}: {}".format(i + 1, argv[i]))
