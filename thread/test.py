#!/usr/bin/env python

__author__ = "anonymous"

import time
import threading

def func():
    for i in range(800000):
        print i,
    print("func done.")

def main1():
    start_time = time.time()
    func()
    func()
    print("main1 done.");
    end_time = time.time()
    print("m1 time " + str(end_time - start_time))

def main2():
    start_time = time.time()
    global t
    for i in range(2):
        t = threading.Thread(target=func)
        t.start()
    t.join()
    print("main2 done.")
    end_time = time.time()
    print("m2 time " + str(end_time - start_time))

if __name__ == "__main__":
    main1()
    main2()
