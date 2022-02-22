# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 15:17:59 2021

@author: dcs839
"""

#### Cross Species Analysis - Generate count tables ###

## Import libs ##

import os
import numpy as np

### Folder and Files ###

## Folders ##

biomart_folder = "lists/Cross Species"

folder_human = "Lists/Samples/Cross species samples/Human"
folder_mouse = "Lists/Samples/Cross species samples/Mouse"
folder_rat = "Lists/Samples/Cross species samples/Rat"

folder_out = "Lists/Count Tables/Cross species"
folder_out_human = "Lists/Count Tables/Cross species/Human"
folder_out_mouse = "Lists/Count Tables/Cross species/Mouse"
folder_out_rat = "Lists/Count Tables/Cross species/Rat"

# if output folder doesn't exists, make one
if os.path.exists(folder_out):
    pass
else:
    os.mkdir(folder_out)
if os.path.exists(folder_out_human):
    pass
else:
    os.mkdir(folder_out_human)
if os.path.exists(folder_out_mouse):
    pass
else:
    os.mkdir(folder_out_mouse)
if os.path.exists(folder_out_rat):
    pass
else:
    os.mkdir(folder_out_rat)

## Files ##

human_file_biomart = "Human_biomart.txt"
mouse_file_biomart = "Mouse_biomart.txt"
rat_file_biomart = "Rat_biomart.txt"

human_file1 = "Sample1_Human_rsem.txt"
human_file2 = "Sample2_Human_rsem.txt"
human_file3 = "Sample3_Human_rsem.txt"
human_file4 = "Sample4_Human_rsem.txt"
human_file5 = "Sample5_Human_rsem.txt"
human_file6 = "Sample6_Human_rsem.txt"

mouse_file1 = "Sample1_Mouse_rsem.txt"
mouse_file2 = "Sample2_Mouse_rsem.txt"
mouse_file3 = "Sample3_Mouse_rsem.txt"
mouse_file4 = "Sample4_Mouse_rsem.txt"
mouse_file5 = "Sample5_Mouse_rsem.txt"
mouse_file6 = "Sample6_Mouse_rsem.txt"
mouse_file7 = "Sample7_Mouse_rsem.txt"
mouse_file8 = "Sample8_Mouse_rsem.txt"
mouse_file9 = "Sample9_Mouse_rsem.txt"

rat_file1 = "Sample3_Rat_rsem.txt"

# File lists #
human_file_list = [human_file1,human_file2,human_file3,human_file4,human_file5,human_file6]

mouse_file_list = [mouse_file1,mouse_file2,mouse_file3,mouse_file4,mouse_file5,mouse_file6,mouse_file7,mouse_file8,mouse_file9]

# Output files #

Human_count_table_all = "Human_count_table_all.csv"
Mouse_count_table_all = "Mouse_count_table_all.csv"

Human_file_out = "CS_Human_TPM.csv"
Mouse_file_out = "CS_Mouse_TPM.csv"
Rat_file_out = "CS_Rat_TPM.csv"


## Global Variables ##

human_biomart = {}
mouse_biomart = {}
rat_biomart = {}

Human_TPM = {}
Mouse_TPM = {}
Rat_TPM = {}

Human_Average_dict = {}
Mouse_Average_dict = {}

### Read files ###

print("Reading biomart - Human")
## Read Human biomart ##
with open(os.path.join(biomart_folder, human_file_biomart),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(",")
        #check if there is dublicates of Ensembl stable gene ids to gene conversion
        if line[0] in human_biomart:
            #if same, just pass
            if human_biomart[line[0]] == line[1].upper():
                pass
            else:
                #if not the same, print the scoundrel and break.
                print(line[0],human_biomart[line[0]],line[1])
                break
        else:
            #if not in dict, add to dict
            human_biomart[line[0]] = line[1].upper()
read.close
print("Done.")
print("Reading biomart - Mouse")
## Read Mouse biomart ##
with open(os.path.join(biomart_folder, mouse_file_biomart),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(",")
        #check if there is dublicates of Ensembl stable gene ids to gene conversion
        if line[0] in mouse_biomart:
            #if same, just pass
            if mouse_biomart[line[0]] == line[1].upper():
                pass
            else:
                #if not the same, print the scoundrel and break.
                print(line[0],mouse_biomart[line[0]],line[1])
                break
        else:
            #if not in dict, add to dict
            mouse_biomart[line[0]] = line[1].upper()
read.close

print("Done.")
print("Reading biomart - rat")

## Read rat biomart ##
with open(os.path.join(biomart_folder, rat_file_biomart),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(",")
        #check if there is dublicates of Ensembl stable gene ids to gene conversion
        if line[0] in rat_biomart:
            #if same, just pass
            if rat_biomart[line[0]] == line[1].upper():
                pass
            else:
                #if not the same, print the scoundrel and break.
                print(line[0],rat_biomart[line[0]],line[1])
                break
        else:
            #if not in dict, add to dict
            rat_biomart[line[0]] = line[1].upper()
read.close

print("Done.")
print("Reading count table - Rat")
## Rat count table ##

with open(os.path.join(folder_rat,rat_file1),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split("\t")
        #Get all values
        if not line[0] in Rat_TPM:
            Rat_TPM[line[0]] = []
            Rat_TPM[line[0]].append(line[5])
        elif line[0] in Rat_TPM:
            Rat_TPM[line[0]].append(line[5])
        else:
            print(line[0])
            break
read.close

print("Done.")
print("Reading count table - Human")
## Human count table all ##
for file in human_file_list:
    with open(os.path.join(folder_human,file),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split("\t")
            #Get all values
            if not line[0] in Human_TPM:
                Human_TPM[line[0]] = []
                Human_TPM[line[0]].append(line[5])
            elif line[0] in Human_TPM:
                Human_TPM[line[0]].append(line[5])
            else:
                print(line[0])
                break
    read.close

print("Done.")
print("Saving count table all - Human")
# Save Human count table all #
with open(os.path.join(folder_out_human,Human_count_table_all),'w+') as out:
    out.write("Ensembl_id;")
    for x in range(1,7,1):
        out.write("CP{};".format(x))
    out.write("\n")
    for key in Human_TPM:
        out.write("{};{}\n".format(key,";".join(Human_TPM[key])))
out.close

print("Done.")
print("Getting average - Human")
# Get average of Human count table #

with open(os.path.join(folder_out_human,Human_count_table_all),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        ## make TPMs float ##
        TPMs = np.array(line[1:],dtype=float)
        ## Get average, decimals ##
        avg = np.round(np.average(TPMs),2)
        ## if average is above zero add to dict
        if avg >= 0.5:
            Human_Average_dict[line[0]] = avg
read.close

print("Done.")
print("Reading count table - Mouse")
## Mouse count table all ##
for file in mouse_file_list:
    with open(os.path.join(folder_mouse,file),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split("\t")
            #Get all values
            if not line[0] in Mouse_TPM:
                Mouse_TPM[line[0]] = []
                Mouse_TPM[line[0]].append(line[5])
            elif line[0] in Mouse_TPM:
                Mouse_TPM[line[0]].append(line[5])
            else:
                print(line[0])
                break
    read.close

print("Done.")
print("Saving count table all - Mouse")

# Save Mouse count table all #
with open(os.path.join(folder_out_mouse,Mouse_count_table_all),'w+') as out:
    out.write("Ensembl_id;")
    for x in range(1,10,1):
        out.write("CP{};".format(x))
    out.write("\n")
    for key in Mouse_TPM:
        out.write("{};{}\n".format(key,";".join(Mouse_TPM[key])))
out.close

print("Done.")
print("Getting average - Mouse")

# Get average of Mouse count table #
with open(os.path.join(folder_out_mouse,Mouse_count_table_all),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        ## make TPMs float ##
        TPMs = np.array(line[1:],dtype=float)
        ## Get average, decimals ##
        avg = np.round(np.average(TPMs),2)
        ## if average is above zero add to dict
        if avg >= 0.5:
            Mouse_Average_dict[line[0]] = avg
read.close

print("Done.")
print("Saving TPM values - Human")

### Save TPM values table to files ###
## Human ##

with open(os.path.join(folder_out_human,Human_file_out),'w+') as out:
    #Add header
    out.write("Ensembl gene id;Gene Symbol;TPM\n")
    for key in Human_Average_dict:
        if human_biomart[key] == '':
            out.write("{};Missing information;{}\n".format(key,str(Human_Average_dict[key]).replace(".",",")))
        else:
            out.write("{};{};{}\n".format(key,human_biomart[key],str(Human_Average_dict[key]).replace(".",",")))
out.close


print("Done.")
print("Saving TPM values - Mouse")

## Mouse ##

with open(os.path.join(folder_out_mouse,Mouse_file_out),'w+') as out:
    #Add header
    out.write("Ensembl gene id;Gene Symbol;TPM\n")
    for key in Mouse_Average_dict:
        if mouse_biomart[key] == '':
            out.write("{};Missing information;{}\n".format(key,str(Mouse_Average_dict[key]).replace(".",",")))
        else:
            out.write("{};{};{}\n".format(key,mouse_biomart[key],str(Mouse_Average_dict[key]).replace(".",",")))
out.close

print("Done.")
print("Saving TPM values - Rat")

## Rat ##

with open(os.path.join(folder_out_rat,Rat_file_out),'w+') as out:
    #Add header
    out.write("Ensembl gene id;Gene Symbol;TPM\n")
    for key in Rat_TPM:
        if float(Rat_TPM[key][0]) >= 0.5:
            if rat_biomart[key] == '':
                out.write("{};Missing information;{}\n".format(key,str(Rat_TPM[key][0]).replace(".",",")))
            else:
                out.write("{};{};{}\n".format(key,rat_biomart[key],str(Rat_TPM[key][0]).replace(".",",")))
        else:
            pass
out.close