# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:21:04 2021

@author: dcs839
"""

### G-Protein-coupled receptors (GPCRs) ###

import os

from operator import itemgetter

### Files and folders ###

## Folders ##

Folder1 = "Lists"
Folder2 = "Lists/Count Tables"
Folder3 = "Results"
Folder4 = "Results/Categories"
Folder5 = "Results/Categories/3.GPCRs"


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

File_targets_and_families = "targets_and_families.csv"

File3_Male = "Sample3_Male_TPM.csv"

File3_out = "Sample3_Male_GPCRs.csv"


### Global variables ###

GPCRs_list_RGD_symbols = []


Male_GPCRs_TPM = {}
Male_GPCRs_Genes = {}


Sorted_Male_gpcrs = []


### load GPCR list ###

with open(os.path.join(Folder1,File_targets_and_families),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split('","')
        if line[0] == '"gpcr':
            if line[18]:
                if line[18].upper() not in GPCRs_list_RGD_symbols:    
                    GPCRs_list_RGD_symbols.append(line[18].upper())
                else:
                    pass
            else:
                pass
        else:
            pass
read.close

### load count tables ###



## Sample 3 - Male ##

with open(os.path.join(Folder2,File3_Male),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        #convert TPM to float
        TPM = float(line[3].replace(",","."))
        #If TPM > 0.5 add, else skip
        if TPM >= 0.5:
            if line[2] in GPCRs_list_RGD_symbols:
                Male_GPCRs_TPM[line[0]] = TPM
                Male_GPCRs_Genes[line[0]] = line[2]
            else:
                pass
        else:
            pass
read.close



### sort GPCR lists by value (TPM)

for key, value in sorted(Male_GPCRs_TPM.items(), key = itemgetter(1,1), reverse = True):
    Sorted_Male_gpcrs.append(key)
    
### Save unfiltrated GPCR lists to files ###

## Sample 3 - Male ##

# Ranking variable initialization #
Rank = 0 

# Save file (sorted based on TPM)
with open(os.path.join(Folder5, File3_out),'w+') as out:
    out.write("Ensembl_id;Gene;TPM;Rank\n")
    for key in Sorted_Male_gpcrs:
        Rank += 1
        out.write("{};{};{};{}\n".format(key,Male_GPCRs_Genes[key],Male_GPCRs_TPM[key],Rank))
out.close
