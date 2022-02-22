# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:03:10 2021

@author: dcs839
"""

#### Protein phosphatases table from evaluation ####

# Import packages #

import os

# Folders #

Folder1 = "Results/Categories/6.Phosphatases/Filtration"
Folder2 = "Results/Categories/6.Phosphatases"

# Files #

File1 = "Evaluation_list_of_Phosphatases.csv"
File2 = "Sample3_Male_Phosphatases.csv"

File3 = "Sample3_Male_Protein_Phosphatases_evaluated.csv"

# Global variables #

Passed_evaluation_Phosphatases = []

Phosphatase_info_dict = {}

## Read files ##

# Evaluation list #
with open(os.path.join(Folder1,File1),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if line[4].lower() == "yes":
            Passed_evaluation_Phosphatases.append(line[0])
        else:
            pass
read.close

# Table content #

with open(os.path.join(Folder2,File2),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if line[0] in Passed_evaluation_Phosphatases:
            Phosphatase_info_dict[line[0]] = line[1:3]
        else:
            pass
read.close

# Save table file #

with open(os.path.join(Folder2,File3),'w+') as out:
    out.write("Ensembl ID;Gene;TPM\n")
    for key in Phosphatase_info_dict:
        out.write("{};{}\n".format(key,";".join(Phosphatase_info_dict[key])))
out.close