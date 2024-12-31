#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 17:54:39 2024

@author: ugurburak
"""

import numpy as np 
import matplotlib.pyplot as plt
import copy

n = 3
oturanlar = []
ayaktakiler = [i for i in range(n)]

s = []
s.append([oturanlar, ayaktakiler])
sayac=0

while len(s) > 0:
    ata = s.pop()
    if len(ata[0])==n:
        print(ata[0], "\n")
        sayac+=1
        continue
    
    for i in range(len(ata[1])):
        yavru = copy.deepcopy(ata)
        yavru[0].append(yavru[1][i])
        yavru[1].remove(yavru[1][i])
        s.append(yavru)
        
print("Çözüm Sayısı", sayac)
