# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 14:37:43 2021

@author: dcs839
"""

### Generate membrane transporter category ###

## import libs ##

import os

### Folder and files ###

## Folders ##

folder1 = "Results/Categories/Unfiltrated"
folder2 = "Results/Categories/Filtrated"
folder3 = "Results/Categories/Transporter and pumps"

if os.path.exists(folder3):
    pass
else:
    os.mkdir(folder3)

## Files ##
    
Filtered_file_FACS = "Sample1_Transport_FACS_Membrane_filtered.csv"
Filtered_file_PT = "Sample2_Transport_PROX_Membrane_filtered.csv"
Filtered_file_Male = "Sample3_Transport_MALE_Membrane_filtered.csv"
Filtered_file_Female = "Sample4_Transport_FEMALE_Membrane_filtered.csv"

Unfiltered_file_FACS = "Sample1_FACS_Transport_unfiltered.csv"
Unfiltered_file_PT = "Sample2_PT_Transport_unfiltered.csv"
Unfiltered_file_Male = "Sample3_Male_Transport_unfiltered.csv"
Unfiltered_file_Female = "Sample4_Female_Transport_unfiltered.csv"

File_out_FACS = "Sample1_FACS_Membrane_Transporter_and_pumps.csv"
File_out_PT = "Sample2_PT_Membrane_Transporter_and_pumps.csv"
File_out_Male = "Sample3_Male_Membrane_Transporter_and_pumps.csv"
File_out_Female = "Sample4_Female_Membrane_Transporter_and_pumps.csv"


## Variables ##

Gene_list_FACS = []
Gene_list_PT = []
Gene_list_Male = []
Gene_list_Female = []
Info_dict_FACS = {}
Info_dict_PT = {}
Info_dict_Male = {}
Info_dict_Female = {}

### Fildered files ###

## Sample 1 - FACS - filtered ##
with open(os.path.join(folder2,Filtered_file_FACS),'r') as read:
     next(read)
     for line in read:
         line = line.strip().split(";")
         Gene_list_FACS.append(line[1])
read.close

## Sample 2 - PT - filtered ##
with open(os.path.join(folder2,Filtered_file_PT),'r') as read:
     next(read)
     for line in read:
         line = line.strip().split(";")
         Gene_list_PT.append(line[1])
read.close

## Sample 3 - Male - filtered ##
with open(os.path.join(folder2,Filtered_file_Male),'r') as read:
     next(read)
     for line in read:
         line = line.strip().split(";")
         Gene_list_Male.append(line[1])
read.close

## Sample 4 - Female - filtered ##
with open(os.path.join(folder2,Filtered_file_Female),'r') as read:
     next(read)
     for line in read:
         line = line.strip().split(";")
         Gene_list_Female.append(line[1])
read.close

### Unfiltered files ###

## Sample 1 - FACS - information from unfiltered ##
with open(os.path.join(folder1,Unfiltered_file_FACS),'r') as read:
     next(read)
     for line in read:
         line = line.strip().split(";")
         Info_dict_FACS[line[1]] = [line[0],line[2]]
read.close

## Sample 1 - PT - information from unfiltered ##
with open(os.path.join(folder1,Unfiltered_file_PT),'r') as read:
     next(read)
     for line in read:
         line = line.strip().split(";")
         Info_dict_PT[line[1]] = [line[0],line[2]]
read.close


## Sample 1 - Male - information from unfiltered ##
with open(os.path.join(folder1,Unfiltered_file_Male),'r') as read:
     next(read)
     for line in read:
         line = line.strip().split(";")
         Info_dict_Male[line[1]] = [line[0],line[2]]
read.close

## Sample 1 - Female - information from unfiltered ##
with open(os.path.join(folder1,Unfiltered_file_Female),'r') as read:
     next(read)
     for line in read:
         line = line.strip().split(";")
         Info_dict_Female[line[1]] = [line[0],line[2]]
read.close

### Save files ###


## Sample1 - FACS ##
Rank = 0
with open(os.path.join(folder3,File_out_FACS),'w+') as out:
    out.write("Ensembl ID;Gene Symbol;TPM;Rank\n")
    for key in Gene_list_FACS:
        Rank += 1
        out.write("{};{};{};{}\n".format(Info_dict_FACS[key][0],key,Info_dict_FACS[key][1],Rank))
out.close

## Sample2 - PT ##
Rank = 0
with open(os.path.join(folder3,File_out_PT),'w+') as out:
    out.write("Ensembl ID;Gene Symbol;TPM;Rank\n")
    for key in Gene_list_PT:
        Rank += 1
        out.write("{};{};{};{}\n".format(Info_dict_PT[key][0],key,Info_dict_PT[key][1],Rank))
out.close

## Sample3 - Male ##
Rank = 0
with open(os.path.join(folder3,File_out_Male),'w+') as out:
    out.write("Ensembl ID;Gene Symbol;TPM;Rank\n")
    for key in Gene_list_Male:
        Rank += 1
        out.write("{};{};{};{}\n".format(Info_dict_Male[key][0],key,Info_dict_Male[key][1],Rank))
out.close

## Sample4 - Female ##
Rank = 0
with open(os.path.join(folder3,File_out_Female),'w+') as out:
    out.write("Ensembl ID;Gene Symbol;TPM;Rank\n")
    for key in Gene_list_Female:
        Rank += 1
        out.write("{};{};{};{}\n".format(Info_dict_Female[key][0],key,Info_dict_Female[key][1],Rank))
out.close