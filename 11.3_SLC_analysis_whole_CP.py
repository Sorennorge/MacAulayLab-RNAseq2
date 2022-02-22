# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 13:15:44 2022

@author: dcs839
"""

### SLC in whole sample of CP ###

## Import packages ##

import os
import re

## Folders ###

Folder1 = "Lists/SLC"
Folder2 = "Lists/Count Tables"
Folder3 = "Results/SLC analysis"

if not os.path.exists(Folder3):
    os.mkdir(Folder3)
else:
    pass

## Files ##

Genes_rat_file = "Sample3_Male_TPM.csv"
SLC_file = "SLC_table.txt"

## Variables ##

Rat_dict = {}
SLC_names = {}

SLC = {}
SLC_Counter = {}

## Read transport and pumps file ##
with open(os.path.join(Folder2,Genes_rat_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";") 
        if not line[0] == '':
            Rat_dict[line[0]] = line[2]
read.close
 
## SLC file ##
with open(os.path.join(Folder1,SLC_file),'r') as read:
    for line in read:
        line = line.strip().split(";") 
        SLC_names[line[0]] = line[1]
read.close

## Add found SLCs together ##

for key in Rat_dict:
    if Rat_dict[key].startswith("SLC"):
        family = re.split("(?<=\d)(?=\D)",Rat_dict[key])
        if family[0].startswith("SLCO"):
            if "SLC21" not in SLC:
                SLC["SLC21"] = 1
                SLC_Counter["SLC21"] = 1
            else:
                SLC["SLC21"] += 1
                SLC_Counter["SLC21"] += 1
        else:
            if family[0] not in SLC:
                SLC[family[0]] = 1
                SLC_Counter[family[0]] = 1
            else:
                SLC[family[0]] += 1
                SLC_Counter[family[0]] += 1
    else:
        pass

