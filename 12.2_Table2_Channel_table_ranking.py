# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:58:35 2021

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

# Facs channels #
File2 = "S4_Supplementary_Tables.csv"

# Female channels #
File3 = "Sample4_Manual_filtration_Female_Membrane_Water_and_ion_channels_evaluated.csv"

# PT channels #
File4 = "S7_Supplementary_Tables.csv"

# Table file #
File5 = "Table2_ranking.csv"

### Global variables ###

Gene_names = {}

Male_channels = []
Facs_channels = []
Female_channels = []
PT_channels = []

Facs_ranking = {}
Female_ranking = {}
PT_ranking = {}

### Read files ###

# Male #
with open(os.path.join(Folder1,File1),'r') as read:
    #for _ in range(1,4,1):
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            Male_channels.append(line[0])
            Gene_names[line[0]] = line[1]
read.close

# Facs #
with open(os.path.join(Folder1,File2),'r') as read:
    #for _ in range(1,4,1):
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            Facs_channels.append(line[0])
read.close
# Female #
with open(os.path.join(Folder2,File3),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            Female_channels.append(line[0])
read.close

# PT #
with open(os.path.join(Folder1,File4),'r') as read:
    #for _ in range(1,4,1):
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            PT_channels.append(line[0])
read.close

for key in Male_channels:
    if key in Facs_channels:
        Facs_ranking[key] = Facs_channels.index(key)+1
    else:
        Facs_ranking[key] = "N/A"
    if key in Female_channels:
        Female_ranking[key] = Female_channels.index(key)+1
    else:
        Female_ranking[key] = "N/A"
    if key in PT_channels:
        PT_ranking[key] = PT_channels.index(key)+1
    else:
        PT_ranking[key] = "N/A"

with open(os.path.join(Folder3,File5),'w+') as out:
    out.write("Ensembl ID;Gene;facs Ranking;Female ranking;PT ranking\n")
    for key in Male_channels:
        out.write("{};{};{};{};{}\n".format(key,Gene_names[key],Facs_ranking[key],Female_ranking[key],PT_ranking[key]))
out.close