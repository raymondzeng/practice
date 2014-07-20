#!/usr/bin/env python2.3
#
#  CodeJamQual.py
#  
#
#  Created by Steven Holte on 9/3/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#

import sys;
import numpy;

file = open(sys.argv[1], 'r')

#Get L D N
LDN = file.readline();
L,D,N = [int(x) for x in LDN.split()];

words = []
Table = [{} for i in range(L)]
for WordI in range(D):
  word = file.readline()[:L]
  words.append(word)
  for i,c in enumerate(word):
    Table[i].setdefault(c,[]).append(WordI)

for case in range(N):
  line = file.readline()
  nextLetter=0
  possible = numpy.zeros(D,'i')
  for letter in range(L):
    if line[nextLetter]=='(':
      nextLetter+=1
      while line[nextLetter]!=')':
        c = line[nextLetter]
        matches=Table[letter].get(line[nextLetter],[])
        for m in matches:
          possible[m]+=1
        nextLetter+=1
      nextLetter+=1
    else:
      matches=Table[letter].get(line[nextLetter],[])
      for m in matches:
        possible[m]+=1
      nextLetter+=1
  choices = (possible==L).sum()
  print "Case #%s: %s"%(case+1,choices)
  




