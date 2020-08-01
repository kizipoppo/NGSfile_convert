#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 2 2020

@author: ShunIto
"""
import cython
import re

def sed(nex):
    cdef int t = 0
    for k in range(len(nex)):
        pattern = r"(?<=charset"+str(t)+":)([\d]*)"
        pattern2 = r"([\d]+)(?=,)"
        if re.search(pattern, nex[k]) != None:
            fore = int(re.search(pattern, nex[k]).group())
            rev = int(re.search(pattern2, nex[k]).group())
            nex[k] = nex[k].replace(str(fore), str(fore+1))
            nex[k] = nex[k].replace(str(rev), str(rev))
            t += 1
    return(nex)
