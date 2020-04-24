#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 2020

@author: ShunIto
"""

import sys
import re
import pandas as pd

def main():
    argvs = sys.argv
    argc = len(argvs)
    if (argc != 3):
        print("Usage: python3 {0} arg1 arg2".format(argvs[0]))
        print("arg1 is working directory.")
        print("arg2 is filename.")
        quit()


    with open(argvs[1] + "/" + argvs[2] + ".txt", "r") as f:
        txt_list = f.readlines()

    patternMig = "Population Index -> Population Label:"
    mig = line_number(txt_list, patternMig)
    pop_list = pop_parser(txt_list[mig + 2].split(" "))
    mig_df = pd.DataFrame(columns=pop_list)
    for k in range(len(pop_list)):
        ser = pd.Series([mig_number(t) for t in txt_list[mig + 6 + k].split(")")[:-1]], index=pop_list)
        mig_df = mig_df.append(ser, ignore_index=True)

    mig_df.index = pop_list
    with open(argvs[1] + "/migrate_" + argvs[2] + ".txt", "w") as f:
        mig_df.to_csv(f, sep="\t")


def line_number(txt_list, pattern):
    k = 0
    for l in txt_list:
        if pattern in l: break
        else: k += 1

    return(k)

def pop_parser(pop_list):
    pop_df = pd.DataFrame(columns=["index", "populations"])
    patternA = r"([0-9A-Za-z.,_-]*)(?=->)"; patternB = r"(?<=->)([0-9A-Za-z.,_-]*)"
    re_patternA = re.compile(patternA)
    re_patternB = re.compile(patternB)
    for t in pop_list:
        if not t: pass
        else:
            ser = pd.Series([re_patternA.search(t).group(), re_patternB.search(t).group()], index=pop_df.columns)
            pop_df = pop_df.append(ser, ignore_index=True)

    pop_df["index"] = pop_df["index"].str.zfill(2)
    pop_df = pop_df.sort_values("index").reset_index(drop=True)
    return(list(pop_df.populations))

def mig_number(mlist_str):
    pattern = r"([0-9.]*)(?=\()"
    re_pattern = re.compile(pattern)
    return(re_pattern.search(mlist_str).group())


if __name__ == '__main__':
    main()
