#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 2 2020

@author: ShunIto
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension('sed', ['sed.pyx'])]
setup(
      name        = 'sed app',
      cmdclass    = {'build_ext':build_ext},
      ext_modules = ext_modules,
      )
