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
[0xE110, 0xE039,     0,     0,   0,   0.94], # Barlines (U+E030–U+E03F)
[0xE10D, 0xE003,     0,     0,   0,   0.94], # Staff brackets and dividers (U+E000–U+E00F)
[0xE17E, 0xE047,     0,     0,   0,   0.94], # Repeats (U+E040–U+E04F)
[0xE129, 0xE048,     0,     0,   0,   0.94],
[0xE12A, 0xE049,     0,     0,   0,   0.94],
[0xE17F, 0xE04A,     0,     0,   0,   0.94],
[0xE11A, 0xE050,     0,     0,   0,   0.94], # Clefs (U+E050–U+E07F)
[0xE117, 0xE05C,     0,     0,   0,   0.94],
[0xE11B, 0xE055,     0,     0,   0,   0.94],
[0xE11C, 0xE056,     0,     0,   0,   0.94],
[0xE118, 0xE061,     0,     0,   0,   0.94],
[0xE119, 0xE062,     0,     0,   0,   0.94],
[0xE11E, 0xE069,     0,     0,   0,   0.94],
[0xE11F, 0xE06A,     0,     0,   0,   0.94],
[0xE11D, 0xE06D,     0,     0,   0,   0.94],
[0xE126, 0xE06E,     0,     0,   0,   0.94],
[0xE123, 0xE07A,     0,     0,   0,   0.94],
[0xE120, 0xE07B,     0,     0,   0,   0.94],
[0xE122, 0xE07C,     0,     0,   0,   0.94],
[0x0030, 0xE080,     0,     0,   0,   0.94], # Time signatures (U+E080–U+E09F)
[0xE10C, 0xE004,     0,     0,   0,   0.94],
[0x0031, 0xE081,     0,     0,   0,   0.94],
[0x0032, 0xE082,     0,     0,   0,   0.94],
[0x0033, 0xE083,     0,     0,   0,   0.94],
[0x0034, 0xE084,     0,     0,   0,   0.94],
[0x0035, 0xE085,     0,     0,   0,   0.94],
[0x0036, 0xE086,     0,     0,   0,   0.94],
[0x0037, 0xE087,     0,     0,   0,   0.94],
[0x0038, 0xE088,     0,     0,   0,   0.94],
[0x0039, 0xE089,     0,     0,   0,   0.94],
[0xE1A7, 0xE08A,     0,     0,   0,   0.94],
[0xE1A6, 0xE08B,     0,     0,   0,   0.94],
[0x002B, 0xE08C,     0,     0,   0,   0.94],
[0x002B, 0xE08D,     0,     0,   0,   0.94],
[0x002D, 0xE090,     0,     0,   0,   0.94],
[0xE104, 0xE092,     0,     0,   0,   0.94],
[0xE105, 0xE093,     0,     0,   0,   0.94],
[0xE104, 0xE094,     0,     0,   0,   0.94],
[0xE105, 0xE095,     0,     0,   0,   0.94],
[0xE116, 0xE0A0,     0,     0,   0,   0.94], # Noteheads (U+E0A0–U+E0FF)
[0xE180, 0xE0A2,     0,     0,   0,   0.94],
[0xE150, 0xE0A3,     0,     0,   0,   0.94],
[0xE14F, 0xE0A4,     0,     0,   0,   0.94],
[0xE1CF, 0xE0A7,     0,     0,   0,   0.94],
[0xE1D0, 0xE0A8,     0,     0,   0,   0.94],
[0xE1D1, 0xE0A9,     0,     0,   0,   0.94],
[0xE1D2, 0xE0B3,     0,     0,   0,   0.94],
[0xE1CA, 0xE0BB,     0,     0,   0,   0.94],
[0xE1CB, 0xE0BC,     0,     0,   0,   0.94],
[0xE1CC, 0xE0BD,     0,     0,   0,   0.94],
[0xE1CD, 0xE0BE,     0,     0,   0,   0.94],
[0xE1C7, 0xE0D8,     0,     0,   0,   0.94],
[0xE1C8, 0xE0D9,     0,     0,   0,   0.94],
[0xE1C9, 0xE0DB,     0,     0,   0,   0.94],
[0xE1C1, 0xE1E7,     0,     0,   0,   0.94], # Individual notes (U+E1D0–U+E1EF)
[0xE102, 0xE220,     0,     0,   0,   0.94], # Tremolos (U+E220–U+E23F)
[0xE197, 0xE240,     0,     0,   0,   0.94], # Flags (U+E240–U+E25F)
[0xE196, 0xE241,     0,     0,   0,   0.94],
[0xE199, 0xE242,     0,     0,   0,   0.94],
[0xE198, 0xE243,     0,     0,   0,   0.94],
[0xE19B, 0xE244,     0,     0,   0,   0.94],
[0xE19A, 0xE245,     0,     0,   0,   0.94],
[0xE19D, 0xE246,     0,     0,   0,   0.94],
[0xE19C, 0xE247,     0,     0,   0,   0.94],
[0xE19F, 0xE248,     0,     0,   0,   0.94],
[0xE19E, 0xE249,     0,     0,   0,   0.94],
[0xE1A1, 0xE24A,     0,     0,   0,   0.94],
[0xE1A0, 0xE24B,     0,     0,   0,   0.94],
[0xE1A3, 0xE24C,     0,     0,   0,   0.94],
[0xE1A2, 0xE24D,     0,     0,   0,   0.94],
[0xE1A5, 0xE24E,     0,     0,   0,   0.94],
[0xE1A4, 0xE24F,     0,     0,   0,   0.94],
[0xE13D, 0xE260,     0,     0,   0,   0.94], # Standard accidentals (U+E260–U+E26F)
[0xE160, 0xE261,     0,     0,   0,   0.94],
[0xE187, 0xE262,     0,     0,   0,   0.94],
[0xE18F, 0xE263,     0,     0,   0,   0.94],
[0xE146, 0xE264,     0,     0,   0,   0.94],
[0xE104, 0xE26A,     0,     0,   0,   0.94],
[0xE105, 0xE26B,     0,     0,   0,   0.94],
[0xE13E, 0xE270,     0,     0,   0,   0.94],
[0xE13F, 0xE271,     0,     0,   0,   0.94],
[0xE161, 0xE272,     0,     0,   0,   0.94],
[0xE162, 0xE273,     0,     0,   0,   0.94],
[0xE189, 0xE274,     0,     0,   0,   0.94],
[0xE18A, 0xE275,     0,     0,   0,   0.94],
[0xE139, 0xE280,     0,     0,   0,   0.94], # Stein-Zimmermann accidentals (24-EDO) (U+E280–U+E28F)
[0xE143, 0xE281,     0,     0,   0,   0.94],
[0xE183, 0xE282,     0,     0,   0,   0.94],
[0xE18C, 0xE283,     0,     0,   0,   0.94],
[0xE142, 0xE440,     0,     0,   0,   0.94], # Arel-Ezgi-Uzdilek (AEU) accidentals (U+E440–U+E44F)
[0xE141, 0xE442,     0,     0,   0,   0.94],
[0xE184, 0xE444,     0,     0,   0,   0.94],
[0xE185, 0xE446,     0,     0,   0,   0.94],
[0xE1B0, 0xE4A0,     0,     0,   0,   0.94], # Articulation (U+E4A0–U+E4BF)
[0xE1B0, 0xE4A1,     0,     0,   0,   0.94],
[0xE192, 0xE4A2,     0,     0,   0,   0.94],
[0xE192, 0xE4A3,     0,     0,   0,   0.94],
[0xE151, 0xE4A4,     0,     0,   0,   0.94],
[0xE151, 0xE4A5,     0,     0,   0,   0.94],
[0xE191, 0xE4A6,     0,     0,   0,   0.94],
[0xE190, 0xE4A7,     0,     0,   0,   0.94],
[0xE1AD, 0xE4AC,     0,     0,   0,   0.94],
[0xE1AE, 0xE4AD,     0,     0,   0,   0.94],
[0xE12B, 0xE4C0,     0,     0,   0,   0.94], #Holds and pauses (U+E4C0–U+E4DF)
[0xE132, 0xE4C1,     0,     0,   0,   0.94],
[0xE12C, 0xE4C2,     0,     0,   0,   0.94],
[0xE12C, 0xE4C3,     0,     0,   0,   0.94],
[0xE12D, 0xE4C4,     0,     0,   0,   0.94],
[0xE134, 0xE4C5,     0,     0,   0,   0.94],
[0xE130, 0xE4C6,     0,     0,   0,   0.94],
[0xE137, 0xE4C7,     0,     0,   0,   0.94],
[0xE131, 0xE4C8,     0,     0,   0,   0.94],
[0xE138, 0xE4C9,     0,     0,   0,   0.94],
[0xE12F, 0xE4CA,     0,     0,   0,   0.94],
[0xE136, 0xE4CB,     0,     0,   0,   0.94],
[0xE12E, 0xE4CC,     0,     0,   0,   0.94],
[0xE135, 0xE4CD,     0,     0,   0,   0.94],
[0xE10E, 0xE4CE,     0,     0,   0,   0.94],
[0xE112, 0xE4CF,     0,     0,   0,   0.94],
[0xE10B, 0xE4D0,     0,     0,   0,   0.94],
[0xE113, 0xE4D1,     0,     0,   0,   0.94],
[0xE115, 0xE4D4,     0,     0,   0,   0.94],
[0xE16B, 0xE4E0,     0,     0,   0,   0.94], # Rests (U+E4E0-U+E4FF)
[0xE16C, 0xE4E1,     0,     0,   0,   0.94],
[0xE16D, 0xE4E2,     0,     0,   0,   0.94],
[0xE17C, 0xE4E3,     0,     0,   0,   0.94],
[0xE178, 0xE4E4,     0,     0,   0,   0.94],
[0xE16F, 0xE4E5,     0,     0,   0,   0.94],
[0xE17A, 0xE4E6,     0,     0,   0,   0.94],
[0xE17B, 0xE4E7,     0,     0,   0,   0.94],
[0xE172, 0xE4E8,     0,     0,   0,   0.94],
[0xE173, 0xE4E9,     0,     0,   0,   0.94],
[0xE174, 0xE4EA,     0,     0,   0,   0.94],
[0xE175, 0xE4EB,     0,     0,   0,   0.94],
[0xE176, 0xE4EC,     0,     0,   0,   0.94],
[0xE177, 0xE4ED,     0,     0,   0,   0.94],
[0xE17D, 0xE4F4,     0,     0,   0,   0.94],
[0xE179, 0xE4F5,     0,     0,   0,   0.94],
[0x0070, 0xE520,     0,     0,   0,   0.94], # Dynamics (U+E520–U+E54F)
[0x006D, 0xE521,     0,     0,   0,   0.94],
[0x0066, 0xE522,     0,     0,   0,   0.94],
[0x0072, 0xE523,     0,     0,   0,   0.94],
[0x0073, 0xE524,     0,     0,   0,   0.94],
[0x007A, 0xE525,     0,     0,   0,   0.94],
[0x006E, 0xE526,     0,     0,   0,   0.94],
[0xE1A8, 0xE566,     0,     0,   0,   0.94], # Common ornaments (U+E560–U+E56F)
[0xE1A9, 0xE567,     0,     0,   0,   0.94],
[0xE1AA, 0xE568,     0,     0,   0,   0.94],
[0xE1AB, 0xE569,     0,     0,   0,   0.94],
[0xE155, 0xE56C,     0,     0,   0,   0.94],
[0xE154, 0xE56D,     0,     0,   0,   0.94],
[0xE156, 0xE56E,     0,     0,   0,   0.94],
[0xE1AC, 0xE56F,     0,     0,   0,   0.94],
[0xE15E, 0xE5B2,     0,     0,   0,   0.94], # Precomposed trills and mordents (U+E5B0–U+E5CF)
[0xE158, 0xE5B5,     0,     0,   0,   0.94],
[0xE159, 0xE5B8,     0,     0,   0,   0.94],
[0xE15D, 0xE5BB,     0,     0,   0,   0.94],
[0xE157, 0xE5BD,     0,     0,   0,   0.94],
[0xE15B, 0xE5C3,     0,     0,   0,   0.94],
[0xE15C, 0xE5C4,     0,     0,   0,   0.94],
[0xE15A, 0xE5C8,     0,     0,   0,   0.94],
[0xE10A, 0xE610,     0,     0,   0,   0.94], # String techniques (U+E610–U+E62F)
[0xE1B7, 0xE612,     0,     0,   0,   0.94],
[0xE14a, 0xE614,     0,     0,   0,   0.94],
[0xE10A, 0xE631,     0,     0,   0,   0.94],
[0xE194, 0xE630,     0,     0,   0,   0.94], # Plucked techniques (U+E630–U+E63F)
[0xE194, 0xE631,     0,     0,   0,   0.94],
[0xE195, 0xE633,     0,     0,   0,   0.94],
[0xE168, 0xE650,     0,     0,   0,   0.94], # Keyboard techniques (U+E650–U+E67F)
[0xE169, 0xE655,     0,     0,   0,   0.94],
[0xE10E, 0xE805,     0,     0,   0,   0.94], # Percussion playing technique pictograms (U+E7F0–U+E80F)
[0xE108, 0xEB78,     0,     0,   0,   0.94], # Arrows and arrowheads (U+EB60–U+EB8F)
[0xE107, 0xEB7C,     0,     0,   0,   0.94],
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
for x in array :
  for i in f.selection.select(x[0]):
    try:
      f.removeGlyph(i)
    except:
      pass
# set name / family and generate target file
f.fontname="GonvilleSmufl";
f.familyname="GonvilleSmufl";
f.generate(argv[2], "opentype");
