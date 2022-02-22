# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:07:54 2021

@author: dcs839
"""

### Evaluate channel table ranking ###

## Import packages ##

import os

### Folders and files ###

## Folders ##

Folder1 = "Results/Supplementary Table/Single sheets"
Folder2 = "Results/Categories/2.Water and ion Channels/Manual Filtration/Evaluated"

Folder3 = "Results/Tables"

# Create output folder if it doesn't exists #
if os.path.exists(Folder3):
    pass
else:
    os.mkdir(Folder3)

## Files ##

# Male channels #
File1 = "S2_Supplementary_Tables.csv"

# PT channels #
File4 = "S7_Supplementary_Tables.csv"

# Table file #
File5 = "Table4_ranking.csv"

### Global variables ###

Gene_names = {}

Male_channels = []
PT_channels = []

Male_ranking = {}


### Read files ###

# Male #
with open(os.path.join(Folder1,File1),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            Male_channels.append(line[0])
read.close


# PT #
with open(os.path.join(Folder1,File4),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            PT_channels.append(line[0])
            Gene_names[line[0]] = line[1]
read.close

for key in list(PT_channels)[:20]:
    if key in Male_channels:
        Male_ranking[key] = Male_channels.index(key)+1
    else:
        Male_ranking[key] = "N/A"

with open(os.path.join(Folder3,File5),'w+') as out:
    out.write("Ensembl ID;Gene;Male ranking\n")
    for key in list(PT_channels)[:20]:
        out.write("{};{};{}\n".format(key,Gene_names[key],Male_ranking[key]))
out.close
