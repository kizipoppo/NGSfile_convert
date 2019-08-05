#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 5 2019

@author: ShunIto
"""

import sys
import pandas as pd
import numpy as np
from str_to_immanc import str_to_immanc as si

def main():
    argvs = sys.argv
    argc = len(argvs)
    if (argc != 3):
        print("Usage: python3 {0} arg1 arg2".format(argvs[0]))
        print("arg1 is working directory.")
        print("arg2 is filename.")
        quit()
    with open(argvs[1] + "/" + argvs[2] + ".str", "r") as f:
        struc = pd.read_table(f, delimiter = "\t")

    pop = [n for n in struc.iloc[:, 0]]
    ind = [n for n in struc.iloc[:, 1]]
    loc = list(struc.columns[2:])
    at = np.array(struc.iloc[:, 2:])
    immanc = si(pop, ind, loc, at)

    with open(argvs[1] + "/" + argvs[2] + ".immanc", "w") as f:
        np.savetxt(f, immanc, delimiter = "\t", fmt="%s")

if __name__ == '__main__':
    main()
