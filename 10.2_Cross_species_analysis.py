# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 12:40:11 2021

@author: dcs839
"""

### Cross species analysis ###

## Import libs ##

import os

### Folder and Files ###

## Folders ##

cross_species_folder = "lists/Cross Species"
count_table_folder_human = "lists/Count Tables/Cross species/Human"
count_table_folder_mouse = "lists/Count Tables/Cross species/Mouse"
count_table_folder_rat = "lists/Count Tables/Cross species/Rat"

output_folder = "Results/Cross species"

# if output folder doesn't exists, make one
if os.path.exists(output_folder):
    pass
else:
    os.mkdir(output_folder)


## Files ##

Human_file = "CS_Human_TPM.csv"
Mouse_file = "CS_Mouse_TPM.csv"
Rat_file = "CS_Rat_TPM.csv"

Ortholog_file = "Ortholog_biomart.txt"

Human_file_out = "Human_shared_rat_protein_coding_genes.csv"
Mouse_file_out = "Mouse_shared_rat_protein_coding_genes.csv"

## Global variable ##

Human_genes_list = []
Rat_genes_list = []
Mouse_genes_list = []

Ortholog_rat_human_dict = {}
Ortholog_rat_mouse_dict = {}

Updated_human_list_orthologs = []
Updated_mouse_list_orthologs = []

## Read files ##

# Rat #
with open(os.path.join(count_table_folder_rat,Rat_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            Rat_genes_list.append(line[0])
read.close

# Human #
with open(os.path.join(count_table_folder_human,Human_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            Human_genes_list.append(line[0])
read.close

# Mouse #
with open(os.path.join(count_table_folder_mouse,Mouse_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            Mouse_genes_list.append(line[0])
read.close

# varible updated genes list for gene conversion #

Updated_human_list_orthologs = Human_genes_list
Updated_mouse_list_orthologs = Mouse_genes_list

## read ortholog biomart ##

with open(os.path.join(cross_species_folder,Ortholog_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(",")
        if not line[1] == '':
            if not line[0] in Ortholog_rat_human_dict:
                Ortholog_rat_human_dict[line[0]] = []
                Ortholog_rat_human_dict[line[0]].append(line[1])
            else:
                Ortholog_rat_human_dict[line[0]].append(line[1])
        if not line[4] == '':
            if not line[0] in Ortholog_rat_mouse_dict:
                Ortholog_rat_mouse_dict[line[0]] = []
                Ortholog_rat_mouse_dict[line[0]].append(line[4])
            else:
                Ortholog_rat_mouse_dict[line[0]].append(line[4])
read.close

## update lists with rat ensembl ids insead of either rat or mouse ##

# Human #
for key in Ortholog_rat_human_dict:
    for item in Ortholog_rat_human_dict[key]:
        if item in Updated_human_list_orthologs:
            if key in Rat_genes_list:
                Updated_human_list_orthologs[Updated_human_list_orthologs.index(item)] = key

# Human #
for key in Ortholog_rat_mouse_dict:
    for item in Ortholog_rat_mouse_dict[key]:
        if item in Updated_mouse_list_orthologs:
            if key in Rat_genes_list:
                Updated_mouse_list_orthologs[Updated_mouse_list_orthologs.index(item)] = key

## Get all genes not shared with Human and mouse ##
shared_rat_human_before_names = list(set(Rat_genes_list) & set(Updated_human_list_orthologs))
Not_shared_rat_human_genes = list(set(Rat_genes_list)-set(shared_rat_human_before_names))

shared_rat_mouse_before_names = list(set(Rat_genes_list) & set(Updated_mouse_list_orthologs))
Not_shared_rat_mouse_genes = list(set(Rat_genes_list)-set(shared_rat_mouse_before_names))


## Read biomarts of rat and human, so we are able to get genes with shared names ##
Rat_human_genes_dict_convertable = {}
Rat_mouse_genes_dict_convertable = {}
Human_genes_dict_convertable = {}
Mouse_genes_dict_convertable = {}

with open(os.path.join(cross_species_folder,"Rat_biomart.txt"),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(",")
        if not line[0] == '':
            if not line[1] == '':
                if line[0] in Not_shared_rat_human_genes:
                    Rat_human_genes_dict_convertable[line[0]] = line[1]
                if line[0] in Not_shared_rat_mouse_genes:
                    Rat_mouse_genes_dict_convertable[line[0]] = line[1]
read.close

with open(os.path.join(cross_species_folder,"Human_biomart.txt"),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(",")
        if not line[0] == '':
            if not line[1] == '':
                Human_genes_dict_convertable[line[0]] = line[1]
read.close

with open(os.path.join(cross_species_folder,"Mouse_biomart.txt"),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(",")
        if not line[0] == '':
            if not line[1] == '':
                Mouse_genes_dict_convertable[line[0]] = line[1]
read.close

### Get shared gene names of Human and rat and update Human gene list ###

# First get genes that are still considered human only genes #
for first_key in Updated_human_list_orthologs:
    if first_key.startswith("ENSG"):
        # if this ensembl id have a gene name
        if first_key in Human_genes_dict_convertable:
            # Go through all ensembl ids for rat and see if there is a uppercase gene name that matches #
            for second_key in Rat_human_genes_dict_convertable:
                # If uppercase human and uppercase rat matches
                if Human_genes_dict_convertable[first_key].upper() == Rat_human_genes_dict_convertable[second_key].upper():
                    #See if this human gene have aldready been replaced, there might be multiple genes in rat that shares same gene name (for some reason) 
                    if first_key in Updated_human_list_orthologs:
                        #if its the first instance of replacing the gene with a rat gene
                        Updated_human_list_orthologs[Updated_human_list_orthologs.index(first_key)] = second_key
                    else:
                        #if there is multiple ensembl with same gene name in rat, append the rat ensembl to the human list to be counted as shared.
                        Updated_human_list_orthologs.append(second_key)

# First get genes that are still considered human only genes #
for first_key in Updated_mouse_list_orthologs:
    if first_key.startswith("ENSMUSG"):
        # if this ensembl id have a gene name
        if first_key in Mouse_genes_dict_convertable:
            # Go through all ensembl ids for rat and see if there is a uppercase gene name that matches #
            for second_key in Rat_mouse_genes_dict_convertable:
                # If uppercase human and uppercase rat matches
                if Mouse_genes_dict_convertable[first_key].upper() == Rat_mouse_genes_dict_convertable[second_key].upper():
                    #See if this human gene have aldready been replaced, there might be multiple genes in rat that shares same gene name (for some reason) 
                    if first_key in Updated_mouse_list_orthologs:
                        #if its the first instance of replacing the gene with a rat gene
                        Updated_mouse_list_orthologs[Updated_mouse_list_orthologs.index(first_key)] = second_key
                    else:
                        #if there is multiple ensembl with same gene name in rat, append the rat ensembl to the human list to be counted as shared.
                        Updated_mouse_list_orthologs.append(second_key)
                        
## Save the Shared gene lists to files for plots ##
# Human #                   
with open(os.path.join(output_folder,Human_file_out),'w+') as out:
    out.write("List of Protein coding genes for human with shared entries with rat as rat ensembl\n")
    for key in Updated_human_list_orthologs:
        if not key == '':
            out.write("{}\n".format(key))
out.close
# Mouse #                   
with open(os.path.join(output_folder,Mouse_file_out),'w+') as out:
    out.write("List of Protein coding genes for mouse with shared entries with rat as rat ensembl\n")
    for key in Updated_mouse_list_orthologs:
        if not key == '':
            out.write("{}\n".format(key))
out.close