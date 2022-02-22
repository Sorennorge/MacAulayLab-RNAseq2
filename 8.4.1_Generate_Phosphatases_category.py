# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:28:45 2021

@author: dcs839
"""

### Phosphatases ###

import os

from operator import itemgetter

### Files and folders ###

## Folders ##

Folder1 = "Lists/Categories/Phosphatases"
Folder2 = "Lists/Count Tables"
Folder3 = "Results"
Folder4 = "Results/Categories"
Folder5 = "Results/Categories/6.Phosphatases"


if not os.path.exists(Folder3):
    os.mkdir(Folder3)
else:
    pass

if not os.path.exists(Folder4):
    os.mkdir(Folder4)
else:
    pass

if not os.path.exists(Folder5):
    os.mkdir(Folder5)
else:
    pass

## Files ##

Phosphatase_list_file = "Phosphatases_ensembl_id_list.txt"

File3_Male = "Sample3_Male_TPM.csv"

File3_out = "Sample3_Male_Phosphatases.csv"


### Global variables ###

Phosphatase_list_RGD_symbols = []

Male_Phosphatases_TPM = {}
Male_Phosphatases_Genes = {}

Sorted_Male_Phosphatases = []

### Load phosphatase list ###

with open(os.path.join(Folder1,Phosphatase_list_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip()
        Phosphatase_list_RGD_symbols.append(line)
read.close

### Load count tables ###

## Sample 3 - Male ##

with open(os.path.join(Folder2,File3_Male),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        #convert TPM to float
        TPM = float(line[3].replace(",","."))
        #If TPM > 0.5 add, else skip
        if TPM >= 0.5:
            if line[0] in Phosphatase_list_RGD_symbols:
                Male_Phosphatases_TPM[line[0]] = TPM
                Male_Phosphatases_Genes[line[0]] = line[2]
            else:
                pass
        else:
            pass
read.close

### Sort phosphatase lists by value (TPM)

for key, value in sorted(Male_Phosphatases_TPM.items(), key = itemgetter(1,1), reverse = True):
    Sorted_Male_Phosphatases.append(key)
    
### Save unfiltrated phosphatase lists to files ###

## Sample 3 - Male ##

# Ranking variable initialization #
Rank = 0 

# Save file (sorted based on TPM)
with open(os.path.join(Folder5, File3_out),'w+') as out:
    out.write("Ensembl_id;Gene;TPM;Rank\n")
    for key in Sorted_Male_Phosphatases:
        Rank += 1
        out.write("{};{};{};{}\n".format(key,Male_Phosphatases_Genes[key],Male_Phosphatases_TPM[key],Rank))
out.close