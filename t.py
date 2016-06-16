#!/usr/bin/env python3
lst = open("netineti/data/grey/species.txt")
grey = frozenset([l.rstrip() for l in lst])
lst = open("netineti/data/white/species.txt")
white = frozenset([l.rstrip() for l in lst])
w = [l for l in white if l not in grey]
for i in w:
   print(i)
