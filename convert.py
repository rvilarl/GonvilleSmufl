#!/usr/bin/python
# usage
# ./conver.py <org> <dst>
#
# convert font formats based on file extension (i.e.: convert GonvilleSmufl.otf GovillleSmufl.woff2)
#

from sys import argv; import fontforge; import psMat; import math
f=fontforge.open(argv[1]);
f.generate(argv[2]);
