# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 13:33:09 2017

@author: Jithu
"""


import datetime
#from collections import Counter
from collections import defaultdict

def file_to_map(path):
    map1 ={}
    with open(path) as f:
        for line in f:
            word,freq = line.split(',')
            map1[word] = int(freq)
        return map1

def merge_maps(map1,map2):
    f = open('out.txt','w')
    map3 = defaultdict(int)
    for d in [map1,map2]:
        for key,val in d.items(): 
            map3[key]+=val
    for key in sorted(map3):        
        f.write("%s,%d\n"%(key,map3[key]))
    f.close()
            
        
a = datetime.datetime.now()   
path1 = raw_input("Enter file1 path: ")
path2 = raw_input("Enter file2 path: ")
fmap1 = {}
fmap2 = {}
fmap1 = file_to_map(path1)
fmap2 = file_to_map(path2)
merge_maps(fmap1,fmap2)
b = datetime.datetime.now()
print b-a