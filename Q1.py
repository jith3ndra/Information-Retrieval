# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:17:54 2017

@author: Jithu
"""
import re
import datetime
from collections import Counter


def tokenize(path):
    #lines = []
    map1 = {}
    with open(path) as f:
        for line in f: 
            #lines += [s.lower() for s in re.findall(r'[\w]+',line)]
            #for word in [s.lower() for s in re.findall(r'[\w]+',line)]:
            for word in [s.lower() for s in re.split('[^a-zA-Z0-9]',line)]:
                if word!= "":
                    if word in map1:
                        map1[word]+= 1
                    else:
                        map1[word] = 1
    #return lines
    return map1

def print_freq(d):
    for key,val in sorted([ (v,k) for k,v in d.iteritems() ],reverse=True):
        print "%s: %d"%(val,key)

   
path1 = raw_input("Enter file1 path: ")
a = datetime.datetime.now()
temp1 = tokenize(path1)
print_freq(temp1)
b = datetime.datetime.now()
print len(temp1)
print b-a