# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 09:15:47 2021

@author: dcs839
"""

#### Protein kinases filtration ####

import os

## Folders ##

Folder1 = "Lists/Filtration lists"

Folder2 = "Results/Categories/5.Kinases"
Folder3 = "Results/Categories/5.Kinases/Filtration"

if os.path.exists(Folder3):
    pass
else:
    os.mkdir(Folder3)

## Files ##

File1 = "Filtration_list_Kinases.csv"
File2 = "Sample3_Male_Kinases.csv"

File3 = "Sample3_Male_Protein_Kinases.csv"

## Global variables ##

kinase_genes = []

Go_term = {}

Protein_kinases = {}

Protein_kinases_dict = {}

# Go terms #
Go_term1 = "protein kinase activity"
Go_term2 = "protein serine/threonine kinase activity"
Go_term3 = "protein serine kinase activity"
Go_term4 = "protein threonine kinase activity"
Go_term5 = "protein tyrosine kinase activity"
Go_term6 = "map kinase activity"

# file list #
Go_term_list = [Go_term1,Go_term2,Go_term3,Go_term4,Go_term5,Go_term6]

## Read files ##
with open(os.path.join(Folder2,File2),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        kinase_genes.append(line[0])
read.close

with open(os.path.join(Folder1,File1),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        Go_term[line[0]] = line[1].split("||")
read.close

## Generate filtration of proteion kinases ##

counter = 0
for key in kinase_genes:
    if key in Go_term:
        protein_kinase_activity_check_list = [0,0,0,0,0,0]
        for item in Go_term[key]:
            if item.lower() == Go_term1:
                protein_kinase_activity_check_list[0] = 1
            if item.lower() == Go_term2:
                protein_kinase_activity_check_list[1] = 1
            if item.lower() == Go_term3:
                protein_kinase_activity_check_list[2] = 1
            if item.lower() == Go_term4:
                protein_kinase_activity_check_list[3] = 1
            if item.lower() == Go_term5:
                protein_kinase_activity_check_list[4] = 1
            if item.lower() == Go_term6:
                protein_kinase_activity_check_list[5] = 1
        if sum(protein_kinase_activity_check_list) == 0:
            Protein_kinases[key] = ""
            Protein_kinases_dict[key] = ""
        elif sum(protein_kinase_activity_check_list) >= 1:
            Protein_kinases[key] = "Protein kinase"
            indexer = 0
            Protein_kinases_dict[key] = []
            for item in protein_kinase_activity_check_list:
                indexer += 1
                if item == 1:
                    Protein_kinases_dict[key].append(Go_term_list[indexer-1])
                else:
                    pass
        else:
            print(key)
            break

## Save file ##

with open(os.path.join(Folder3,File3),'w+') as out:
    out.write("Gene;protein kinases check;Go terms\n")
    for key in kinase_genes:
        out.write("{};{};{}\n".format(key,Protein_kinases[key],"||".join(Protein_kinases_dict[key])))
out.close