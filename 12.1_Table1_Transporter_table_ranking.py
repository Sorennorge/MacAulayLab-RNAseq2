# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:14:47 2021

@author: dcs839
"""

### Evaluate transporter table ranking ###

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

# Facs transporters #
File2 = "S3_Supplementary_Tables.csv"

# Female transporters #
File3 = "Sample4_Manual_filtration_Female_Membrane_Transporter_and_pumps_evaluated.csv"

# PT transporters #
File4 = "S6_Supplementary_Tables.csv"

# Table file #
File5 = "Table1_ranking.csv"

### Global variables ###

Gene_names = {}

Male_transporters = []
Facs_transporters = []
Female_transporters = []
PT_transporters = []

Facs_ranking = {}
Female_ranking = {}
PT_ranking = {}

### Read files ###

# Male #
with open(os.path.join(Folder1,File1),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            Male_transporters.append(line[0])
            Gene_names[line[0]] = line[1]
read.close

# Facs #
with open(os.path.join(Folder1,File2),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            Facs_transporters.append(line[0])
read.close
# Female #
with open(os.path.join(Folder2,File3),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            Female_transporters.append(line[0])
read.close

# PT #
with open(os.path.join(Folder1,File4),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            PT_transporters.append(line[0])
read.close

for key in Male_transporters:
    if key in Facs_transporters:
        Facs_ranking[key] = Facs_transporters.index(key)+1
    else:
        Facs_ranking[key] = "N/A"
    if key in Female_transporters:
        Female_ranking[key] = Female_transporters.index(key)+1
    else:
        Female_ranking[key] = "N/A"
    if key in PT_transporters:
        PT_ranking[key] = PT_transporters.index(key)+1
    else:
        PT_ranking[key] = "N/A"

with open(os.path.join(Folder3,File5),'w+') as out:
    out.write("Ensembl ID;Gene;facs Ranking;Female ranking;PT ranking\n")
    for key in Male_transporters:
        out.write("{};{};{};{};{}\n".format(key,Gene_names[key],Facs_ranking[key],Female_ranking[key],PT_ranking[key]))
out.close
        