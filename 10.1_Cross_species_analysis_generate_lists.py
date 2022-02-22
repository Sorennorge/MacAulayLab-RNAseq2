# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 11:06:42 2021

@author: dcs839
"""

### Cross species Analysis ###

## Import libs ##

import os

### Folder and Files ###

## Folders ##

cross_species_folder = "lists/Cross Species"

folder_human = "Lists/Count Tables/Human"
folder_mouse = "Lists/Count Tables/Mouse"
folder_rat = "Lists/Count Tables"

cross_species_folder_out = "lists/Cross Species/Protein coding"

# if output folder doesn't exists, make one
if os.path.exists(cross_species_folder):
    pass
else:
    os.mkdir(cross_species_folder)


## Files ##

Human_file = "Human_TPM.csv"
Mouse_file = "Mouse_TPM.csv"
Rat_file = "Sample3_Male_TPM.csv"

Protein_rat = "Biomart_protein_coding_rat.txt"
Protein_human = "Biomart_protein_coding_human.txt"
Protein_mouse = "Biomart_protein_coding_mouse.txt"

Out_Human_file = "Human_sample_Protein_coding_genes.csv"
Out_Mouse_file = "Mouse_sample_Protein_coding_genes.csv"
Out_Rat_file = "Rat_sample_Protein_coding_genes.csv"

## Global variable ##

Rat_protein_coding = []
Human_protein_coding = []
Mouse_protein_coding = []

Sample_rat_pc_list = []
Sample_human_pc_list = []
Sample_mouse_pc_list = []

### Read files ###
## Protein coding lists ##
# Rat #
with open(os.path.join(cross_species_folder,Protein_rat),'r') as read:
    next(read)
    for line in read:
        line = line.strip()
        if not line == '':
            Rat_protein_coding.append(line)
read.close
# Human #
with open(os.path.join(cross_species_folder,Protein_human),'r') as read:
    next(read)
    for line in read:
        line = line.strip()
        if not line == '':
            Human_protein_coding.append(line)
read.close
# Rat #
with open(os.path.join(cross_species_folder,Protein_mouse),'r') as read:
    next(read)
    for line in read:
        line = line.strip()
        if not line == '':
            Mouse_protein_coding.append(line)
read.close

## Sample files ##

Sample_mouse_pc_list = []

# Rat #
with open(os.path.join(folder_rat,Rat_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            if float(line[3].replace(",",".")) >= 0.5:
                if line[0] in Rat_protein_coding:
                    Sample_rat_pc_list.append(line[0])
                else:
                    pass
            else:
                pass
        else:
            pass
read.close

# Human #
with open(os.path.join(folder_human,Human_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            if line[0] in Human_protein_coding:
                Sample_human_pc_list.append(line[0])
            else:
                pass
        else:
            pass
read.close
# Mouse #
with open(os.path.join(folder_mouse,Mouse_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            if line[0] in Mouse_protein_coding:
                Sample_mouse_pc_list.append(line[0])
            else:
                pass
        else:
            pass
read.close

### Save Protein coding genes to files ###

# Rat #
with open(os.path.join(cross_species_folder_out,Out_Rat_file),'w') as out:
    out.write("Protein coding genes in Rat\n")
    for key in Sample_rat_pc_list:
        out.write("{}\n".format(key))
out.close

# Human #
with open(os.path.join(cross_species_folder_out,Out_Human_file),'w') as out:
    out.write("Protein coding genes in Human\n")
    for key in Sample_human_pc_list:
        out.write("{}\n".format(key))
out.close

# Mouse #
with open(os.path.join(cross_species_folder_out,Out_Mouse_file),'w') as out:
    out.write("Protein coding genes in Mouse\n")
    for key in Sample_mouse_pc_list:
        out.write("{}\n".format(key))
out.close