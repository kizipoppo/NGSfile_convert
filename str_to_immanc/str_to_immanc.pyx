#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 5 2019

@author: ShunIto
"""
import numpy as np
cimport numpy as np

def str_to_immanc(pop, ind, loc, table):

    cdef int nind=len(table), k=0
    cdef list pop_array=[], ind_array=[], loc_array=[]
    cdef np.ndarray dat = np.zeros([nind*table.shape[1], 2], int)

    for n in range(table.shape[1]):
        for i in range(nind):
            pop_array.append(pop[i*2])
            ind_array.append(ind[i*2])
            loc_array.append(loc[n])
            dat[k, 0] = table[i, n*2]
            dat[k, 1] = table[i, n*2+1]
            k += 1

    cdef np.ndarray file = npDataFrame(pop_array, ind_array, loc_array, dat, k)
    return(file)

cdef npDataFrame(pop_array, ind_array, loc_array, dat, k):
    cdef np.ndarray ind = np.array(ind_array).reshape((k,1))
    cdef np.ndarray pop = np.array(pop_array).reshape((k,1))
    cdef np.ndarray loc = np.array(loc_array).reshape((k,1))
    cdef np.ndarray immanc = np.hstack((ind, pop, loc, dat))
    return(immanc)
