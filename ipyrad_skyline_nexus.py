#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 29 2020

@author: ShunIto
"""
import sys
import re
import random
import pandas as pd

def main():
    argvs = sys.argv
    argc = len(argvs)
    if (argc != 8):
        print("Usage: python3 {0} arg1 arg2".format(argvs[0]))
        print("arg1 is working directory.")
        print("arg2 is filename.")
        print("arg3 is maximum number of SNPs.")
        print("arg4 is minimum number of SNPs.")
        print("arg5 is the number of sampling.")
        print("arg6 is the number of loci.")
        print("arg7 is random seed.")
        quit()

    # cut off the SNPs based on threshold values.
    if (int(argvs[3])==0) & (int(argvs[4])==0):
        if (int(argvs[6]) == int(argvs[5])):
            samp = [t for t in range(1, int(argvs[6])+1)]
        else:
            snpsnum = read_snpsmap(argvs[1], argvs[2]).index
            samp = [t for t in range(1, int(argvs[6]) + 1)]
            for k in snpsnum:
                samp.remove(k)
    else:
        snpsnum = read_snpsmap(argvs[1], argvs[2])
        snpsnum = snpsnum[(snpsnum <= int(argvs[3])) & (snpsnum >= int(argvs[4]))]
        snpsnum = list(snpsnum.index)
        # random sampling
        random.seed(int(argvs[7]))
        samp = random.sample(snpsnum, int(argvs[5]))

    # check the number of loci.
    if len(samp) < int(argvs[5]):
        print("The number of sampling is lower than that of loci.\n")
        print("The number of selected loci is " + str(len(samp)) + ".")
    else:
        # load the loci file.
        lf = select_loci(argvs[1] + "/" + argvs[2] + ".gphocs")
        for k in samp:
            lf.extract_loci(k-1)
            lf.init()
        print("Completed!!")


class select_loci:
    def __init__(self, loci_file):
        with open(loci_file, "r") as f:
            self.loci_file = f.readlines()
        self.k = 0

    def extract_loci(self, num):
        pattern = r"(?<=locus" + str(num) + ")([\d\s]*)"
        for l in self.loci_file:
            if re.search(pattern, l) != None:
                lab = re.search(pattern, l).group().split(" ")
                create_nexus(num, lab[1], lab[2].replace("\n", ""))
                self.k += 1
                f = open("locus" + str(num) + ".nexus", "a")
                for t in range(self.k, self.k+int(lab[1])):
                    f.write(self.loci_file[t])
                f.close()
                end_nexus(num)
                break
            else:
                self.k += 1

    def init(self):
        self.k = 0

def read_snpsmap(wd, filename):
    # load a snpsmap file.
    with open(wd + "/" + filename + ".snpsmap", "r") as f:
        snpsmap = pd.read_table(f, delimiter="\t", header=None)
    # rename the columns of snpsmap.
    snpsmap.columns = ["locus", "locus_position", "position", "num"]
    # count the number of SNPs per loci and return the pandas.Series.
    snpsnum = snpsmap.locus.value_counts()
    return(snpsnum)


def create_nexus(num, NTAX, NCHAR):
    f = open("locus"+ str(num) + ".nexus", "w")
    f.write("#NEXUS\n\n")
    f.write("BEGIN DATA;\n")
    params = "DIMENSIONS  NTAX=" + str(NTAX) + " NCHAR=" + str(NCHAR) + ";\n"
    f.write(params)
    f.write("FORMAT DATATYPE=DNA GAP=- MISSING=?;\n")
    f.write("MATRIX\n\n")
    f.close()

def end_nexus(num):
    f = open("locus" + str(num) + ".nexus", "a")
    f.write(";\n\n")
    f.write("END;\n")
    f.close()


if __name__ == "__main__":
    main()
