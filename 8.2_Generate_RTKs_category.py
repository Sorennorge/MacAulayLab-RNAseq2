# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:27:39 2021

@author: dcs839
"""

### RTKs ###

## Import packages ##

import os

from operator import itemgetter

### Files and folders ###

## Folders ##

Folder1 = "Lists"
Folder2 = "Lists/Count Tables"
Folder3 = "Results"
Folder4 = "Results/Categories"
Folder5 = "Results/Categories/4.RTKs"

Info_folder = "Lists/Categories/RTKs"

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

Info_file1 = "RTK_HGNC.csv"
Info_file2 = "RTK_HGNC_subgroup.csv"
Info_file3 = "Human_HGNC_to_Rat_ensembl.txt"

File3_Male = "Sample3_Male_TPM.csv"

File3_out = "Sample3_Male_RTKs.csv"


### Global variables ###

RTKs_dict = {}

RTK_ensembl_list = []
RTK_information_check = {}

Male_RTKs_TPM = {}
Male_RTKs_Genes = {}


Sorted_Male_RTKs = []


### load RTK list ###

with open(os.path.join(Info_folder,Info_file1),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if line[0] not in RTKs_dict:
            RTKs_dict[line[0]] = line[1]
        else:
            print(line[0])
            print("Error case 1: dublicates")
            break
read.close

with open(os.path.join(Info_folder,Info_file2),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if line[0] not in RTKs_dict:
            RTKs_dict[line[0]] = line[1]
        else:
            print(line[0])
            print("Error case 1: dublicates")
            break
read.close


with open(os.path.join(Info_folder,Info_file3),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(",")
        if line[1] in RTKs_dict:
            if line[4] not in RTK_ensembl_list:
                RTK_ensembl_list.append(line[4])    
            RTK_information_check[line[1]] = line[4]
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
            if line[0] in RTK_ensembl_list:
                Male_RTKs_TPM[line[0]] = TPM
                Male_RTKs_Genes[line[0]] = line[2]
            else:
                pass
        else:
            pass
read.close

### sort RTK lists by value (TPM)

for key, value in sorted(Male_RTKs_TPM.items(), key = itemgetter(1,1), reverse = True):
    Sorted_Male_RTKs.append(key)
    
### Save unfiltrated RTK lists to files ###

## Sample 3 - Male ##

# Ranking variable initialization #
Rank = 0 

# Save file (sorted based on TPM)
with open(os.path.join(Folder5, File3_out),'w+') as out:
    out.write("Ensembl_id;Gene;TPM;Rank\n")
    for key in Sorted_Male_RTKs:
        Rank += 1
        out.write("{};{};{};{}\n".format(key,Male_RTKs_Genes[key],Male_RTKs_TPM[key],Rank))
out.close