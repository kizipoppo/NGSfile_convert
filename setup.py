#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 5 2019

@author: ShunIto
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

ext_modules = [Extension('str_to_immanc', ['str_to_immanc.pyx'])]   #assign new.pyx module in setup.py.
setup(
      name        = 'str_to_immanc app',
      cmdclass    = {'build_ext':build_ext},
      ext_modules = ext_modules,
      include_dirs = [np.get_include()]
      )