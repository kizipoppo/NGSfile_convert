#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 2 2020

@author: ShunIto
"""
import sys
import re
from sed import sed

def main():
    argvs = sys.argv
    argc = len(argvs)
    if (argc != 2):
        print("Usage: python3 {0} arg1".format(argvs[0]))
        print("arg1 is filename")
        quit()

    with open("imm.nex", "r") as f:
        nex = f.readlines()

    nex = sed(nex)
    with open(argvs[1], "w") as f:
        f.writelines(nex)

if __name__ == "__main__":
    main()
