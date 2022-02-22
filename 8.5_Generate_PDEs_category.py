# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:21:04 2021

@author: dcs839
"""

### Phosphodiesterases (PDEs) ###

import os

from operator import itemgetter

### Files and folders ###

## Folders ##

Folder1 = "Lists"
Folder2 = "Lists/Count Tables"
Folder3 = "Results"
Folder4 = "Results/Categories"
Folder5 = "Results/Categories/7.PDEs"


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

File3_Male = "Sample3_Male_TPM.csv"

File3_out = "Sample3_Male_PDEs.csv"


### Global variables ###

Male_PDEs_TPM = {}
Male_PDEs_Genes = {}


Sorted_Male_PDEs = []


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
            if line[2].startswith("PDE"):
                Male_PDEs_TPM[line[0]] = TPM
                Male_PDEs_Genes[line[0]] = line[2]
            else:
                pass
        else:
            pass
read.close



### sort PDE lists by value (TPM)

for key, value in sorted(Male_PDEs_TPM.items(), key = itemgetter(1,1), reverse = True):
    Sorted_Male_PDEs.append(key)
    
### Save unfiltrated PDE lists to files ###

## Sample 3 - Male ##

# Ranking variable initialization #
Rank = 0 

# Save file (sorted based on TPM)
with open(os.path.join(Folder5, File3_out),'w+') as out:
    out.write("Ensembl_id;Gene;TPM;Rank\n")
    for key in Sorted_Male_PDEs:
        Rank += 1
        out.write("{};{};{};{}\n".format(key,Male_PDEs_Genes[key],Male_PDEs_TPM[key],Rank))
out.close
