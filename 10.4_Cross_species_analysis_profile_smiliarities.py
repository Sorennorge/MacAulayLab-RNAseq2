# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

### Cross species similarities ###

## Import libs ##

import os

### Folder and Files ###

## Folders ##

count_table_folder_human = "lists/Count Tables/Cross species/Human"
count_table_folder_mouse = "lists/Count Tables/Cross species/Mouse"
count_table_folder_rat = "lists/Count Tables/Cross species/Rat"
folder2 = "Results/Cross species"
folder3 = "Results/Cross species/Similarities"

if os.path.exists(folder3):
    pass
else:
    os.mkdir(folder3)

## Files ##

Rat_file = "CS_Rat_TPM.csv"
Human_file = "CS_Human_TPM.csv"
Mouse_file = "CS_Mouse_TPM.csv"

Compared_Human_file = "Human_shared_rat_protein_coding_genes.csv"
Compared_Mouse_file = "Mouse_shared_rat_protein_coding_genes.csv"

## Global variables ##

Rat_TPM_dict = {}
Human_TPM_dict = {}
Mouse_TPM_dict = {}

Not_shared_Human_list = []
Not_shared_Mouse_list = []

Rat_sum = 0
Human_sum = 0
Mouse_sum = 0

## Read count tables ##

# Rat #
with open(os.path.join(count_table_folder_rat,Rat_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            Rat_TPM_dict[line[0]] = float(line[2].replace(",","."))
            Rat_sum += float(line[2].replace(",","."))
read.close

# Human #
with open(os.path.join(count_table_folder_human,Human_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            Human_TPM_dict[line[0]] = float(line[2].replace(",","."))
            Human_sum += float(line[2].replace(",","."))
read.close

# Mouse #
with open(os.path.join(count_table_folder_mouse,Mouse_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            Mouse_TPM_dict[line[0]] = float(line[2].replace(",","."))
            Mouse_sum += float(line[2].replace(",","."))
read.close


Rat_sum = round(Rat_sum,2)
Human_sum = round(Human_sum,2)
Mouse_sum = round(Mouse_sum,2)

## Read comparison files ##

with open(os.path.join(folder2,Compared_Human_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip()
        if not line[0] == '':
            Not_shared_Human_list.append(line)
read.close

with open(os.path.join(folder2,Compared_Mouse_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip()
        if not line[0] == '':
            Not_shared_Mouse_list.append(line)
read.close

Not_shared_Human_list = list(set(Not_shared_Human_list))

Not_shared_Mouse_list = list(set(Not_shared_Mouse_list))

TPM_RAT_not_in_Human = 0
TPM_Human_not_in_rat = 0

TPM_RAT_not_in_Mouse = 0
TPM_Mouse_not_in_rat = 0

Gene_list_not_shared_human = []
Gene_list_not_shared_Mouse = []
Not_shared_rat_list_with_human = []
Not_shared_rat_list_with_mouse = []

for key in Not_shared_Human_list:
    if key in Human_TPM_dict:
        TPM_Human_not_in_rat += Human_TPM_dict[key]
        Gene_list_not_shared_human.append(key)

for key in Not_shared_Mouse_list:
    if key in Mouse_TPM_dict:
        TPM_Mouse_not_in_rat += Mouse_TPM_dict[key]
        Gene_list_not_shared_Mouse.append(key)
for key in Rat_TPM_dict:
    if key not in Not_shared_Human_list:
        TPM_RAT_not_in_Human += Rat_TPM_dict[key]
        Not_shared_rat_list_with_human.append(key)
    if key not in Not_shared_Mouse_list:
        TPM_RAT_not_in_Mouse += Rat_TPM_dict[key]
        Not_shared_rat_list_with_mouse.append(key)
        
with open(os.path.join(folder3,"Summary_file.txt"),'w+') as out:
    out.write("Summary file of shared TPM profile\n")
    out.write("Percentage of Human not shared: {}\n".format(round(TPM_Human_not_in_rat/Human_sum*100,2)))
    out.write("Percentage of rat not shared with Human: {}\n".format(round(TPM_RAT_not_in_Human/Rat_sum*100,2)))
    out.write("Percentage of Human not shared: {}\n".format(round(TPM_Mouse_not_in_rat/Mouse_sum*100,2)))
    out.write("Percentage of rat not shared with Human: {}\n".format(round(TPM_RAT_not_in_Mouse/Rat_sum*100,2)))
out.close

with open(os.path.join(folder3,"Gene_list_not_shared_human.txt"),'w+') as out:
    for key in Gene_list_not_shared_human:
        out.write("{}\n".format(key))
out.close

with open(os.path.join(folder3,"Gene_list_not_shared_Mouse.txt"),'w+') as out:
    for key in Gene_list_not_shared_Mouse:
        out.write("{}\n".format(key))
out.close

with open(os.path.join(folder3,"Gene_list_for_rat_not_shared_human.txt"),'w+') as out:
    for key in Not_shared_rat_list_with_human:
        out.write("{}\n".format(key))
out.close

with open(os.path.join(folder3,"Gene_list_for_rat_not_shared_Mouse.txt"),'w+') as out:
    for key in Not_shared_rat_list_with_mouse:
        out.write("{}\n".format(key))
out.close