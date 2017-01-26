# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 09:52:32 2017

@author: Jithu
"""
import re
import datetime
from collections import Counter


def tokenize(path):
    lines = set()
    with open(path) as f:
        for line in f: 
            lines.update([s.lower() for s in re.findall(r'[\w]+',line)])
    return lines

path1 = raw_input("Enter file1 path: ")
path2 = raw_input("Enter file2 path: ")
a = datetime.datetime.now()  
temp1 = tokenize(path1)
temp2 = tokenize(path2)


common = temp1.intersection(temp2)
print common
print len(common)
b = datetime.datetime.now()
print b-a