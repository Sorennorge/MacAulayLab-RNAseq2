# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 15:21:44 2021

@author: dcs839
"""

## Import packages ##

import os
import re

## Folders ###

Folder1 = "Lists/SLC"
Folder2 = "Results/Categories/1.Transporter and pumps"
Folder3 = "Results/SLC analysis"

if not os.path.exists(Folder3):
    os.mkdir(Folder3)
else:
    pass

## Files ##

Genes_rat_file = "Sample3_Male_Membrane_Transporter_and_pumps_evaluated.csv"
SLC_file = "SLC_table.txt"

File_out = "SLC_list_Sample3_Male.csv"

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
            Rat_dict[line[0]] = [line[1],line[2],float(line[3])]
read.close
 
## SLC file ##
with open(os.path.join(Folder1,SLC_file),'r') as read:
    for line in read:
        line = line.strip().split(";") 
        SLC_names[line[0]] = line[1]
read.close

## Add found SLCs together ##

for key in Rat_dict:
    if Rat_dict[key][0].startswith("SLC"):
        family = re.split("(?<=\d)(?=\D)",Rat_dict[key][0])
        if family[0].startswith("SLCO"):
            if "SLC21" not in SLC:
                SLC["SLC21"] = Rat_dict[key][2]
                SLC_Counter["SLC21"] = 1
            else:
                SLC["SLC21"] += Rat_dict[key][2]
                SLC_Counter["SLC21"] += 1
        else:
            if family[0] not in SLC:
                SLC[family[0]] = Rat_dict[key][2]
                SLC_Counter[family[0]] = 1
            else:
                SLC[family[0]] += Rat_dict[key][2]
                SLC_Counter[family[0]] += 1
    elif Rat_dict[key][1].startswith("SLC"):
        family = re.split("(?<=\d)(?=\D)",Rat_dict[key][1])
        if family[0].startswith("SLCO"):
            if "SLC21" not in SLC:
                SLC["SLC21"] = Rat_dict[key][2]
                SLC_Counter["SLC21"] = 1
            else:
                SLC["SLC21"] += Rat_dict[key][2]
                SLC_Counter["SLC21"] += 1
        else:
            if family[0] not in SLC:
                SLC[family[0]] = Rat_dict[key][2]
                SLC_Counter[family[0]] = 1
            else:
                SLC[family[0]] += Rat_dict[key][2]
                SLC_Counter[family[0]] += 1
    else:
        pass

## Sort SLC list ##
Sorted_SLC = sorted(SLC.items(), key=lambda x: x[1], reverse=True)

## Save SLC list to file ##

with open(os.path.join(Folder3,File_out),'w+') as out:
    out.write("Family Name;SLC;Number of SLC;Accumulated Expression (TPM)\n")
    for key in Sorted_SLC:
        if key[0] in SLC_names:
            out.write("{};{};{};{}\n".format(SLC_names[key[0]],key[0],SLC_Counter[key[0]],str(round(key[1],2)).replace(".",",")))
        else:
            out.write("Error;{};{};{};\n".format(key[0],SLC_Counter[key[0]],str(round(key[1],2)).replace(".",",")))
out.close
