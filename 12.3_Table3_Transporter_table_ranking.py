# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 08:48:00 2021

@author: dcs839
"""

### Table 3 - Transporter Ranking ###

## Import packages ##

import os

### Folders and files ###

## Folders ##

Folder1 = "Results/Supplementary Table/Single sheets"
Folder2 = "Results/Categories/1.Transporter and pumps/Manual Filtration/Evaluated"

Folder3 = "Results/Tables"

# Create output folder if it doesn't exists #
if os.path.exists(Folder3):
    pass
else:
    os.mkdir(Folder3)

## Files ##

# Male transporters #
File1 = "S1_Supplementary_Tables.csv"


# PT transporters #
File4 = "S6_Supplementary_Tables.csv"

# Table file #
File5 = "Table3_ranking.csv"

### Global variables ###

Gene_names = {}

Male_transporters = []
PT_transporters = []

Male_ranking = {}

### Read files ###

# Male #
with open(os.path.join(Folder1,File1),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            Male_transporters.append(line[0])
read.close

# PT #
with open(os.path.join(Folder1,File4),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            PT_transporters.append(line[0])
            Gene_names[line[0]] = line[1]
read.close

for key in list(PT_transporters)[:20]:
    if key in Male_transporters:
        Male_ranking[key] = Male_transporters.index(key)+1
    else:
        Male_ranking[key] = "N/A"

with open(os.path.join(Folder3,File5),'w+') as out:
    out.write("Ensembl ID;Gene;Male Ranking\n")
    for key in list(PT_transporters)[:20]:
        out.write("{};{};{}\n".format(key,Gene_names[key],Male_ranking[key]))
out.close
        