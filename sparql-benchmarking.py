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


def vivo_query(query, parms):
    """
    A VIVO query function using SPARQLWrapper. Authenticates, adds a VIVO prefix, and returns JSON.
    :param query: SPARQL query.  VIVO PREFIX will be added
    :param parms: dictionary with query parms:  queryuri, username and password
    :return: result object, typically JSON
    :rtype: dict
    """
    from SPARQLWrapper import SPARQLWrapper, JSON

    sparql = SPARQLWrapper(parms['queryuri'])
    new_query = parms['prefix'] + '\n' + query
    sparql.setQuery(new_query)
    sparql.setReturnFormat(JSON)
    sparql.addParameter("email", parms['username'])
    sparql.addParameter("password", parms['password'])
    results = sparql.query()
    results = results.convert()
    return results


def read_test(test):
    if test == 'test.rq':
        for i in range(1000000):
            i += 1
    elif test == 'conlon':
        for i in range(100000):
            i += 1
    elif test == 'write':
        for i in range(50000):
            i += 1
    elif test == "load":
        for i in range(50000):
            x = i/2.0
    return


def main():

    start = time.time()
    config = configparser.ConfigParser()
    config.read("sparql-benchmarking.properties")
    stop = time.time()
    print("Time to read properties", stop-start)
    f = open("sparql-benchmarking.tsv", "w")
    f.write("function\tname\tsize\trepeat\tduration\n")

#   Read tests

    repeat = int(config.get("READ", "repeat"))
    sizes = config.get("READ", "sizes").replace(" ", "").split(",")
    test_names = config.get("READ", "sparql").replace(" ", "").split(",")
    print(test_names)
    for test in test_names:
        for size in sizes:
            # Generate data of requested size. Empty and reload VIVO
            r = 1
            while r <= repeat:
                start = time.time()
                # execute the test
                read_test(test)
                stop = time.time()
                duration = stop - start
                f.write("READ" + "\t" + test + "\t" + size + "\t" + str(r) + "\t" + str(duration) + "\n")
                r += 1

#   Write tests

    repeat = int(config.get("WRITE", "repeat"))
    sizes = config.get("WRITE", "sizes").replace(" ", "").split(",")
    test = "write"
    for size in sizes:
        # Generate data of requested size
        r = 1
        while r <= repeat:
            start = time.time()
            # execute the test
            read_test(test)
            stop = time.time()
            duration = stop - start
            f.write("WRITE" + "\t" + test + "\t" + size + "\t" + str(r) + "\t" + str(duration) + "\n")
            r += 1

#   Load Tests

    repeat = int(config.get("LOAD", "repeat"))
    sizes = config.get("LOAD", "sizes").replace(" ", "").split(",")
    test = "load"
    for size in sizes:
        # Generate data of requested size
        r = 1
        while r <= repeat:
            start = time.time()
            # execute the test
            read_test(test)
            stop = time.time()
            duration = stop - start
            f.write("LOAD" + "\t" + test + "\t" + size + "\t" + str(r) + "\t" + str(duration) + "\n")
            r += 1

    f.close()


if __name__ == "__main__":
    main()
