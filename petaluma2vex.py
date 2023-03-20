#!/usr/bin/python
# usage
# ./gonville2smufl.py <org> <dst>
#

from sys import argv; import fontforge; import psMat; import math
# array[0..5]
# [0] original glyph position
# [1] target glyph position (as per SMuFL standard)
# [2] x translation of origin
# [3] y translation of origin
# [4] rotation in degrees
# [5] scale ( 1 means 100% no scale  )
#
array=[
[0xE080, 0xE080,     0,     0,   0,   0.70], # Time signatures (U+E080–U+E09F)
[0xE081, 0xE081,     0,     0,   0,   0.70],
[0xE082, 0xE082,     0,     0,   0,   0.70],
[0xE083, 0xE083,     0,     0,   0,   0.70],
[0xE084, 0xE084,     0,     0,   0,   0.70],
[0xE085, 0xE085,     0,     0,   0,   0.70],
[0xE086, 0xE086,     0,     0,   0,   0.70],
[0xE087, 0xE087,     0,     0,   0,   0.70],
[0xE088, 0xE088,     0,     0,   0,   0.70],
[0xE089, 0xE089,     0,     0,   0,   0.70],
[0xE08C, 0xE08C,     0,     0,   0,   0.70],
[0xE08D, 0xE08D,     0,     0,   0,   0.70],
[0xE090, 0xE090,     0,     0,   0,   0.70],
]
f=fontforge.open(argv[1]);
for x in array :
  # copy and paste
  f.selection.select(x[0]);
  f.copy();
  f.selection.select(x[1]);
  f.paste();
  # apply translation of origin
  if x[2] != 0 or x[3] != 0:
    matrix = psMat.translate(x[2],x[3])
    for i in f.selection:
      f[i].transform(matrix)
  # rotate
  if x[4] != 0:
    matrix = psMat.rotate(math.radians(x[4]))
    for i in f.selection:
      f[i].transform(matrix)
  # scale
  if x[5] != 1:
    matrix = psMat.scale(x[5])
    for i in f.selection:
      f[i].transform(matrix)
# remove glyphs in original position
# for x in array :
#   for i in f.selection.select(x[0]):
#     try:
#       f.removeGlyph(i)
#     except:
#       pass
# set name / family and generate target file
f.fontname="PetalumaVex";
f.familyname="PetalumaVex";
f.generate(argv[2], "opentype");
