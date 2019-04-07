#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Sun Apr 19 10:53:47 2015

delete duplicate files! to be used with the command fdupes on linux, redirecting its output to the file dupes
fdupes . > dupes

@author: mat
"""

import os
import time

cwd = os.getcwd()
print(cwd)

t0 = time.ctime()
print(t0)

filename = "dupes"

size = 0
nb_f = 0

with open(filename, 'r') as f:
    contents = f.readlines()

i = 0
while i<len(contents):
    line = contents[i][:-1]  # remove the \n
    if "savephone/Pictures" in line:
        print("rm", line)
        size += os.stat(line).st_size
        # os.remove(line)
        
        nb_f += 1
        
    i += 1



print(nb_f, size)
