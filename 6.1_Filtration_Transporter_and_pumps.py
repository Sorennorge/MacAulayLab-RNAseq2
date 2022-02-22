# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 10:24:14 2021

@author: dcs839
"""

### Transport filtration ###


## import libs ##

import os

### Folder and files ###

## Folders ##

folder1 = "Lists/Filtration lists"
folder2 = "Results/Categories/Unfiltrated"
folder3 = "Results/Categories/Filtrated"

if os.path.exists(folder3):
    pass
else:
    os.mkdir(folder3)

## Files ##

Transporter_filtration_list = "Filtration_list_Transporter_and_pumps.csv"

# Files input #
Sample1_file_FACS = "Sample1_FACS_Transport_unfiltered.csv"
Sample2_file_PT = "Sample2_PT_Transport_unfiltered.csv"
Sample3_file_Male = "Sample3_Male_Transport_unfiltered.csv"
Sample4_file_Female = "Sample4_Female_Transport_unfiltered.csv"

# Files output #
Filtered_file_FACS = "Sample1_Transport_FACS_Membrane_filtered.csv"
Filtered_file_PT = "Sample2_Transport_PROX_Membrane_filtered.csv"
Filtered_file_Male = "Sample3_Transport_MALE_Membrane_filtered.csv"
Filtered_file_Female = "Sample4_Transport_FEMALE_Membrane_filtered.csv"

## Global variables ##

FACS_genes = {}
PT_genes = {}
Male_genes = {}
Female_genes = {}

Genes_of_interest_FACS = {}
Genes_of_interest_PT = {}
Genes_of_interest_Male = {}
Genes_of_interest_Female = {}

## Sample 1 - FACS ##
with open(os.path.join(folder2,Sample1_file_FACS),'r') as read:
     next(read)
     for line in read:
         line = line.strip().split(";")
         FACS_genes[line[0]] = line[1]
read.close

## Sample 2 - Proximal tubules ##
with open(os.path.join(folder2,Sample2_file_PT),'r') as read:
     next(read)
     for line in read:
         line = line.strip().split(";")
         PT_genes[line[0]] = line[1]
read.close

## Sample 3 - Male ##
with open(os.path.join(folder2,Sample3_file_Male),'r') as read:
     next(read)
     for line in read:
         line = line.strip().split(";")
         Male_genes[line[0]] = line[1]
read.close

## Sample 4 - Female ##
with open(os.path.join(folder2,Sample4_file_Female),'r') as read:
     next(read)
     for line in read:
         line = line.strip().split(";")
         Female_genes[line[0]] = line[1]
read.close


with open(os.path.join(folder1,Transporter_filtration_list),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(';')
    
        ## Sample 1 - FACS - membrane filtration ##
        
        if line[0] in FACS_genes:
            # If genes startswith "SLC25" (mitochondrial), or "atp5" (mitochondrial) or "atp6v" (vacuolar type atp) skip entries
            if not FACS_genes[line[0]].startswith('SLC25') and not FACS_genes[line[0]].startswith('atp5'.upper()) and not FACS_genes[line[0]].startswith('atp6v'.upper()):
                # If Cellular Component (CC) is empty - Add empty tag
                if line[1] == '':
                    Genes_of_interest_FACS[line[0]] = 'Empty tag'
                # If Cellular Component (CC) contains plasma membrane tag - add Plasma membrane tag 
                elif "integral component of plasma membrane".upper() in line[1].upper() or "plasma membrane".upper() in line[1].upper():
                    Genes_of_interest_FACS[line[0]] = 'Plasma membrane tag'
                # If Cellular Component (CC) contains membrane tag, but is not part of lysosome, endosome, mitochondrial,gologi, vacular - add Filtered tag
                elif ("integral component of membrane".upper() in line[1].upper() or "membrane".upper() in line[1].upper() or "transmembrane".upper() in line[1].upper()):
                    if not ("lysosome".upper() in line[1].upper() or "endosome membrane".upper() in line[1].upper() or "lysosomal".upper() in line[1].upper()):
                        if not ("mitochondrion".upper() in line[1].upper() or "mitochondrial".upper() in line[1].upper()):
                            if not ("golgi apparatus".upper() in line[1].upper() or "vacuolar".upper() in line[1].upper() or "endoplasmic".upper() in line[1].upper()):
                                Genes_of_interest_FACS[line[0]] = 'Filtered tag'
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
        
        ## Sample 2 - Proximal tubules - membrane filtration ##
        
        if line[0] in PT_genes:
            # If genes startswith "SLC25" (mitochondrial), or "atp5" (mitochondrial) or "atp6v" (vacuolar type atp) skip entries (bit redundant, for PT, Male, and female)
            if not PT_genes[line[0]].startswith('SLC25') and not PT_genes[line[0]].startswith('atp5'.upper()) and not PT_genes[line[0]].startswith('atp6v'.upper()):
                # If Cellular Component (CC) is empty - Add empty tag
                if line[1] == '':
                    Genes_of_interest_PT[line[0]] = 'Empty tag'
                # If Cellular Component (CC) contains plasma membrane tag - add Plasma membrane tag 
                elif "integral component of plasma membrane".upper() in line[1].upper() or "plasma membrane".upper() in line[1].upper():
                    Genes_of_interest_PT[line[0]] = 'Plasma membrane tag'
                # If Cellular Component (CC) contains membrane tag, but is not part of lysosome, endosome, mitochondrial,gologi, vacular - add Filtered tag
                elif ("integral component of membrane".upper() in line[1].upper() or "membrane".upper() in line[1].upper() or "transmembrane".upper() in line[1].upper()):
                    if not ("lysosome".upper() in line[1].upper() or "endosome membrane".upper() in line[1].upper() or "lysosomal".upper() in line[1].upper()):
                        if not ("mitochondrion".upper() in line[1].upper() or "mitochondrial".upper() in line[1].upper()):
                            if not ("golgi apparatus".upper() in line[1].upper() or "vacuolar".upper() in line[1].upper() or "endoplasmic".upper() in line[1].upper()):
                                Genes_of_interest_PT[line[0]] = 'Filtered tag'
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
        
        ## Sample 3 - Male - membrane filtration ##
        
        if line[0] in Male_genes:
            # If genes startswith "SLC25" (mitochondrial), or "atp5" (mitochondrial) or "atp6v" (vacuolar type atp) skip entries (bit redundant, for PT, Male, and female)
            if not Male_genes[line[0]].startswith('SLC25') and not Male_genes[line[0]].startswith('atp5'.upper()) and not Male_genes[line[0]].startswith('atp6v'.upper()):
                # If Cellular Component (CC) is empty - Add empty tag
                if line[1] == '':
                    Genes_of_interest_Male[line[0]] = 'Empty tag'
                # If Cellular Component (CC) contains plasma membrane tag - add Plasma membrane tag 
                elif "integral component of plasma membrane".upper() in line[1].upper() or "plasma membrane".upper() in line[1].upper():
                    Genes_of_interest_Male[line[0]] = 'Plasma membrane tag'
                # If Cellular Component (CC) contains membrane tag, but is not part of lysosome, endosome, mitochondrial,gologi, vacular - add Filtered tag
                elif ("integral component of membrane".upper() in line[1].upper() or "membrane".upper() in line[1].upper() or "transmembrane".upper() in line[1].upper()):
                    if not ("lysosome".upper() in line[1].upper() or "endosome membrane".upper() in line[1].upper() or "lysosomal".upper() in line[1].upper()):
                        if not ("mitochondrion".upper() in line[1].upper() or "mitochondrial".upper() in line[1].upper()):
                            if not ("golgi apparatus".upper() in line[1].upper() or "vacuolar".upper() in line[1].upper() or "endoplasmic".upper() in line[1].upper()):
                                Genes_of_interest_Male[line[0]] = 'Filtered tag'
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
        
        ## Sample 4 - Female - membrane filtration ##
        
        if line[0] in Female_genes:
            # If genes startswith "SLC25" (mitochondrial), or "atp5" (mitochondrial) or "atp6v" (vacuolar type atp) skip entries (bit redundant, for PT, Male, and female)
            if not Female_genes[line[0]].startswith('SLC25') and not Female_genes[line[0]].startswith('atp5'.upper()) and not Female_genes[line[0]].startswith('atp6v'.upper()):
                # If Cellular Component (CC) is empty - Add empty tag
                if line[1] == '':
                    Genes_of_interest_Female[line[0]] = 'Empty tag'
                # If Cellular Component (CC) contains plasma membrane tag - add Plasma membrane tag 
                elif "integral component of plasma membrane".upper() in line[1].upper() or "plasma membrane".upper() in line[1].upper():
                    Genes_of_interest_Female[line[0]] = 'Plasma membrane tag'
                # If Cellular Component (CC) contains membrane tag, but is not part of lysosome, endosome, mitochondrial,gologi, vacular - add Filtered tag
                elif ("integral component of membrane".upper() in line[1].upper() or "membrane".upper() in line[1].upper() or "transmembrane".upper() in line[1].upper()):
                    if not ("lysosome".upper() in line[1].upper() or "endosome membrane".upper() in line[1].upper() or "lysosomal".upper() in line[1].upper()):
                        if not ("mitochondrion".upper() in line[1].upper() or "mitochondrial".upper() in line[1].upper()):
                            if not ("golgi apparatus".upper() in line[1].upper() or "vacuolar".upper() in line[1].upper() or "endoplasmic".upper() in line[1].upper()):
                                Genes_of_interest_Female[line[0]] = 'Filtered tag'
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
read.close


### Save filtered lists to files ###

## Sample 1 - FACS - filtered ##
with open(os.path.join(folder3,Filtered_file_FACS),'w+') as out:
    out.write("Ensembl id;Gene;Filtration tag\n")
    for key in Genes_of_interest_FACS:
        out.write("{};{};{}\n".format(key,FACS_genes[key],Genes_of_interest_FACS[key]))
out.close

## Sample 2 - Proximal tubules - filtered ##

with open(os.path.join(folder3,Filtered_file_PT),'w+') as out:
    out.write("Ensembl id;Gene;Filtration tag\n")
    for key in Genes_of_interest_PT:
        out.write("{};{};{}\n".format(key,PT_genes[key],Genes_of_interest_PT[key]))
out.close

## Sample 3 - Male - filtered ##

with open(os.path.join(folder3,Filtered_file_Male),'w+') as out:
    out.write("Ensembl id;Gene;Filtration tag\n")
    for key in Genes_of_interest_Male:
        out.write("{};{};{}\n".format(key,Male_genes[key],Genes_of_interest_Male[key]))
out.close

## Sample 4 - Female - filtered ##

with open(os.path.join(folder3,Filtered_file_Female),'w+') as out:
    out.write("Ensembl id;Gene;Filtration tag\n")
    for key in Genes_of_interest_Female:
        out.write("{};{};{}\n".format(key,Female_genes[key],Genes_of_interest_Female[key]))
out.close
