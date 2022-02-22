# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 15:13:16 2021

@author: dcs839
"""

### Cyclases ###

import os

from operator import itemgetter

### Files and folders ###

## Folders ##

Folder1 = "Lists/Categories/Cyclases"
Folder2 = "Lists/Count Tables"
Folder3 = "Results"
Folder4 = "Results/Categories"
Folder5 = "Results/Categories/8.Cyclases"


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

Cyclase_list_file = "Cyclase_ensembl_id_list.txt"

File3_Male = "Sample3_Male_TPM.csv"

File3_out = "Sample3_Male_Cyclases.csv"


### Global variables ###

Cyclase_list_RGD_symbols = []

Male_Cyclases_TPM = {}
Male_Cyclases_Genes = {}

Sorted_Male_Cyclases = []

### Load cyclase list ###

with open(os.path.join(Folder1,Cyclase_list_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip()
        Cyclase_list_RGD_symbols.append(line)
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
            if line[0] in Cyclase_list_RGD_symbols:
                Male_Cyclases_TPM[line[0]] = TPM
                Male_Cyclases_Genes[line[0]] = line[2]
            else:
                pass
        else:
            pass
read.close

### Sort cyclase lists by value (TPM)

for key, value in sorted(Male_Cyclases_TPM.items(), key = itemgetter(1,1), reverse = True):
    Sorted_Male_Cyclases.append(key)
    
### Save unfiltrated cyclase lists to files ###

## Sample 3 - Male ##

# Ranking variable initialization #
Rank = 0 

# Save file (sorted based on TPM)
with open(os.path.join(Folder5, File3_out),'w+') as out:
    out.write("Ensembl_id;Gene;TPM;Rank\n")
    for key in Sorted_Male_Cyclases:
        Rank += 1
        out.write("{};{};{};{}\n".format(key,Male_Cyclases_Genes[key],Male_Cyclases_TPM[key],Rank))
out.close