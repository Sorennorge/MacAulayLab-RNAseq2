# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 09:15:47 2021

@author: dcs839
"""

#### Protein Phosphatases filtration ####

import os

## Folders ##

Folder1 = "Lists/Filtration lists"

Folder2 = "Results/Categories/6.Phosphatases"
Folder3 = "Results/Categories/6.Phosphatases/Filtration"

if os.path.exists(Folder3):
    pass
else:
    os.mkdir(Folder3)

## Files ##

File1 = "Filtration_list_Phosphatases.csv"
File2 = "Sample3_Male_Phosphatases.csv"

File3 = "Sample3_Male_Protein_Phosphatases.csv"

# Global variables #

Phosphatase_genes = []

Go_term = {}

Protein_Phosphatases = {}

Protein_Phosphatases_dict = {}

# Go terms #
Go_term1 = "phosphoprotein phosphatase activity"
Go_term2 = "protein serine/threonine phosphatase activity"
Go_term3 = "protein serine phosphatase activity"
Go_term4 = "protein threonine phosphatase activity"
Go_term5 = "protein tyrosine phosphatase activity"

# File list #
Go_term_list = [Go_term1,Go_term2,Go_term3,Go_term4,Go_term5]

## Read files ##
with open(os.path.join(Folder2,File2),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        Phosphatase_genes.append(line[0])
read.close

with open(os.path.join(Folder1,File1),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        Go_term[line[0]] = line[1].split("||")
read.close

## Generate filtration of proteion Phosphatases ##

counter = 0
for key in Phosphatase_genes:
    if key in Go_term:
        protein_Phospha_activity_check_list = [0,0,0,0,0]
        for item in Go_term[key]:
            if item.lower() == Go_term1:
                protein_Phospha_activity_check_list[0] = 1
            if item.lower() == Go_term2:
                protein_Phospha_activity_check_list[1] = 1
            if item.lower() == Go_term3:
                protein_Phospha_activity_check_list[2] = 1
            if item.lower() == Go_term4:
                protein_Phospha_activity_check_list[3] = 1
            if item.lower() == Go_term5:
                protein_Phospha_activity_check_list[4] = 1
        if sum(protein_Phospha_activity_check_list) == 0:
            Protein_Phosphatases[key] = ""
            Protein_Phosphatases_dict[key] = ""
        elif sum(protein_Phospha_activity_check_list) >= 1:
            Protein_Phosphatases[key] = "Protein Phosphatase"
            indexer = 0
            Protein_Phosphatases_dict[key] = []
            for item in protein_Phospha_activity_check_list:
                indexer += 1
                if item == 1:
                    Protein_Phosphatases_dict[key].append(Go_term_list[indexer-1])
                else:
                    pass
        else:
            print(key)
            break

## Save file ##

with open(os.path.join(Folder3,File3),'w+') as out:
    out.write("Gene;protein Phosphatases check;Go terms\n")
    for key in Phosphatase_genes:
        out.write("{};{};{}\n".format(key,Protein_Phosphatases[key],"||".join(Protein_Phosphatases_dict[key])))
out.close