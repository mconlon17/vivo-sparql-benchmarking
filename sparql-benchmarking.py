#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    vivo-sparql-benchmarking: generate timing for read, write, and load of data in VIVO

    All options are set in the properties file, sparql-benchmarking.properties

    sparql-benchmarking.py writes timing data to sparql-benchmarking.tsv.  Each row represents a test condition.  Columns
    indicate the parameters of the test and the resulting time to complete.  The file can be used in data analytic
    software such as R to generate plots and statistics.

"""

import configparser
import time

__author__ = "Michael Conlon"
__copyright__ = "Copyright (c) 2019 Michael Conlon"
__license__ = "Apache-2"
__version__ = "0.0.0"

def main():

    start = time.time()
    config = configparser.ConfigParser()
    config.read("sparql-benchmarking.properties")
    stop = time.time()
    print("Time to read properties", stop-start)
    f = open("sparql-benchmarking.tsv", "w")

#   Read tests

    repeat = int(config.get("READ", "repeat"))
    while repeat > 0:
        f.write("READ" + "\t" + str(repeat) + "\n")
        repeat -= 1

#   Write tests

    repeat = int(config.get("WRITE", "repeat"))
    while repeat > 0:
        f.write("WRITE" + "\t" + str(repeat) + "\n")
        repeat -= 1

#   Load Tests

    repeat = int(config.get("LOAD", "repeat"))
    while repeat > 0:
        f.write("LOAD" + "\t" + str(repeat) + "\n")
        repeat -= 1

    f.close()


if __name__ == "__main__":
    main()
