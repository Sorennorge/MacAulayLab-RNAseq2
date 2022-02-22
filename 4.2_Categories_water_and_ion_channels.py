# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 14:21:53 2021

@author: dcs839
"""

### Get Water and ion channels ###

### Channels ###

### list from https://www.guidetopharmacology.org/ ###

import os

from operator import itemgetter

### Files and folders ###

## Folders ##
Folder1 = "Lists"
Folder2 = Folder1+"/Count Tables"
Folder3 = "Results"
Folder4 = Folder3+"/Categories"
Folder5 = Folder4+"/Unfiltrated"

# If output folders doesn't exists -> create them #
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
# Input files #
File_targets_and_families = "targets_and_families.csv"

File1_FACS = "Sample1_FACS_TPM.csv"
File2_PT = "Sample2_PT_TPM.csv"
File3_Male = "Sample3_Male_TPM.csv"
File4_Female = "Sample4_Female_TPM.csv"

# Output files #
File1_out = "Sample1_FACS_channels_unfiltered.csv"
File2_out = "Sample2_PT_channels_unfiltered.csv"
File3_out = "Sample3_Male_channels_unfiltered.csv"
File4_out = "Sample4_Female_channels_unfiltered.csv"

### Global variables ###

Channels_list_RGD_symbols = []

FACS_channels_TPM = {}
FACS_channels_Genes = {}

PT_channels_TPM = {}
PT_channels_Genes = {}

Male_channels_TPM = {}
Male_channels_Genes = {}

Female_channels_TPM = {}
Female_channels_Genes = {}

Sorted_Male_channels = []
Sorted_FACS_channels = []
Sorted_PT_channels = []
Sorted_Male_channels = []
Sorted_Female_channels = []

### load Transport list ###

with open(os.path.join(Folder1,File_targets_and_families),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split('","')
        if line[0] == '"vgic' or line[0] == '"lgic' or line[0] == '"other_ic':
            if line[18]:
                if line[18].upper() not in Channels_list_RGD_symbols:    
                    Channels_list_RGD_symbols.append(line[18].upper())
                else:
                    pass
            else:
                pass
        else:
            pass
read.close

### load count tables ###

## Sample 1 - FACS ##

with open(os.path.join(Folder2,File1_FACS),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        #convert TPM to float
        TPM = float(line[3].replace(",","."))
        #If TPM > 0.5 add, else skip
        if TPM >= 0.5:
            if line[2] in Channels_list_RGD_symbols:
                FACS_channels_TPM[line[0]] = TPM
                FACS_channels_Genes[line[0]] = line[2]
            else:
                pass
        else:
            pass
read.close

## Sample 2 - Proximal tubules ##

with open(os.path.join(Folder2,File2_PT),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        #convert TPM to float
        TPM = float(line[3].replace(",","."))
        #If TPM > 0.5 add, else skip
        if TPM >= 0.5:
            if line[2] in Channels_list_RGD_symbols:
                PT_channels_TPM[line[0]] = TPM
                PT_channels_Genes[line[0]] = line[2]
            else:
                pass
        else:
            pass
read.close

## Sample 3 - Male ##

with open(os.path.join(Folder2,File3_Male),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        #convert TPM to float
        TPM = float(line[3].replace(",","."))
        #If TPM > 0.5 add, else skip
        if TPM >= 0.5:
            if line[2] in Channels_list_RGD_symbols:
                Male_channels_TPM[line[0]] = TPM
                Male_channels_Genes[line[0]] = line[2]
            else:
                pass
        else:
            pass
read.close

## Sample 4 - Female ##

with open(os.path.join(Folder2,File4_Female),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        #convert TPM to float
        TPM = float(line[3].replace(",","."))
        #If TPM > 0.5 add, else skip
        if TPM >= 0.5:
            if line[2] in Channels_list_RGD_symbols:
                Female_channels_TPM[line[0]] = TPM
                Female_channels_Genes[line[0]] = line[2]
            else:
                pass
        else:
            pass
read.close

### sort transport lists by value (TPM)
for key, value in sorted(FACS_channels_TPM.items(), key = itemgetter(1,1), reverse = True):
    Sorted_FACS_channels.append(key)

for key, value in sorted(PT_channels_TPM.items(), key = itemgetter(1,1), reverse = True):
    Sorted_PT_channels.append(key)

for key, value in sorted(Male_channels_TPM.items(), key = itemgetter(1,1), reverse = True):
    Sorted_Male_channels.append(key)
    
for key, value in sorted(Female_channels_TPM.items(), key = itemgetter(1,1), reverse = True):
    Sorted_Female_channels.append(key)

### Save unfiltrated transport lists to files ###

## Sample 1 - FACS ##

# Ranking variable initialization #
Rank = 0 

# Save file (sorted based on TPM)
with open(os.path.join(Folder5, File1_out),'w+') as out:
    out.write("Ensembl_id;Gene;TPM;Rank\n")
    for key in Sorted_FACS_channels:
        Rank += 1
        out.write("{};{};{};{}\n".format(key,FACS_channels_Genes[key],FACS_channels_TPM[key],Rank))
out.close

## Sample 2 - Proximal tubules ##

# Ranking variable initialization #
Rank = 0 

# Save file (sorted based on TPM)
with open(os.path.join(Folder5, File2_out),'w+') as out:
    out.write("Ensembl_id;Gene;TPM;Rank\n")
    for key in Sorted_PT_channels:
        Rank += 1
        out.write("{};{};{};{}\n".format(key,PT_channels_Genes[key],PT_channels_TPM[key],Rank))
out.close

## Sample 3 - Male ##

# Ranking variable initialization #
Rank = 0 

# Save file (sorted based on TPM)
with open(os.path.join(Folder5, File3_out),'w+') as out:
    out.write("Ensembl_id;Gene;TPM;Rank\n")
    for key in Sorted_Male_channels:
        Rank += 1
        out.write("{};{};{};{}\n".format(key,Male_channels_Genes[key],Male_channels_TPM[key],Rank))
out.close

## Sample 4 - Female ##

# Ranking variable initialization #
Rank = 0 

# Save file (sorted based on TPM)
with open(os.path.join(Folder5, File4_out),'w+') as out:
    out.write("Ensembl_id;Gene;TPM;Rank\n")
    for key in Sorted_Female_channels:
        Rank += 1
        out.write("{};{};{};{}\n".format(key,Female_channels_Genes[key],Female_channels_TPM[key],Rank))
out.close
