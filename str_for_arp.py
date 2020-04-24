#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 5 2020

@author: ShunIto
"""

import sys
import pandas as pd
import numpy as np

def main():
    argvs = sys.argv
    argc = len(argvs)
    if (argc != 4):
        print("Usage: python3 {0} arg1 arg2".format(argvs[0]))
        print("arg1 is working directory of .")
        print("arg2 is structure file name.")
        print("arg3 is population file name.")
        quit()
    with open(argvs[1]  + "/" + argvs[2]  + ".str", "r") as f:
        struc = pd.read_table(f, delimiter = "\t", header=None,
                              dtype={0:str})

    with open(argvs[1]  + "/" + argvs[3] + ".txt", "r") as f:
        pop = pd.read_table(f, delimiter = "\t", dtype={"id":str})

    struc = struc.drop(range(1,5), axis=1)
    struc.columns = struc.columns.map(str)
    struc = struc.rename(columns={"0":"id"})
    struc.id = [code.strip() for code in struc.id]
    struc = pd.merge(pop, struc, on="id", how="left")

    struc.iloc[:,2:].astype(int)

    with open(argvs[1] + "/arp_" + argvs[2] + ".str", "w") as f:
        struc.to_csv(f, sep = "\t", index=None, header=True)

if __name__ == '__main__':
    main()