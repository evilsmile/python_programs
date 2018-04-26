#!/usr/bin/env python
__author__ = "anonymous"

import time
import multiprocessing

def func():
    i = 0
    for _ in range(20000000):
        i += 1
    print("fun done.")

def main1():
    start_time = time.time()
    func()
    func()
    print("main1 execute done.")
    end_time = time.time()
    print("m1 time:" + str(end_time - start_time))


def main2():
    start_time = time.time()
    for i in range(2):
        p = multiprocessing.Process(target=func)
        p.start()
    p.join()
    print("main2 execute done.")
    end_time = time.time()
    print("m2 time:" + str(end_time - start_time))

if __name__ == "__main__":
    main1()
    main2()
