#!/usr/bin/env python
from sys import argv

foo = int(argv[1])
a = []
for x in range(1, foo):
 if not foo % x:
  a.append([x, foo/x])


print a
  
