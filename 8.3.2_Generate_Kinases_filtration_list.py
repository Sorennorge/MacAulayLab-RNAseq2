# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 08:56:36 2021

@author: dcs839
"""

### Filtration list -- Kinases ##

## Import libs ##

import os
import mygene

## Functions ##

mg = mygene.MyGeneInfo()

## folder and files ##

# Folders #

Folder = "Results/Categories/5.Kinases"

Folder_out = "Lists/Filtration lists"


# Files #

File = "Sample3_Male_Kinases.csv"

File_out = "Filtration_list_Kinases.csv"

# Global variables #

Kinase_genes = []
Info_list = {}

# Read kinase file #
with open(os.path.join(Folder,File),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] in Kinase_genes:
            Kinase_genes.append(line[0])
        else:
            pass
read.close

### Cellular Component (CC) ##
## Get CC for ensembl entries to use for location filtration ##
with open(os.path.join(Folder_out,File_out),'w+',encoding="utf-8") as out:
    out.write("ID;MF\n")
    # initialize counter #
    counter = 0
    for key in Kinase_genes:
        ## progress info ##
        counter += 1
        print("{} - {}/{}".format(key,counter,len(Kinase_genes)))
        ### Get lookup values ###
        ## Initialize ##
        lookup = []
        
        try:
            lookup = mg.getgene(key)
        except:
            print("Case 2: {}".format(key))
            break
        ### Initialize dicts ###
        
        ## Info_list ##
        Info_list[key] = []

        
        ## Complete info list ##
        
        # If not data #
        if not lookup:
            out.write("{};\n".format(key))
            continue
        
        ### Handle Go terms ###
        # If there is lookup table #
        if lookup:
            if 'go' in lookup.keys():
                ### Handle CC ###
                if 'MF' in lookup['go']:
                    if lookup['go']['MF']:
                        if not 'term' in lookup['go']['MF']:
                            for item in lookup['go']['MF']:
                                if 'term' in item:
                                    if item['term'].lower() not in Info_list[key]:
                                        Info_list[key].append(item['term'].lower())
                        else:
                            if lookup['go']['MF']['term'].lower() not in Info_list[key]:
                                Info_list[key].append(lookup['go']['MF']['term'].lower())
                    else:
                        pass
                else:
                    pass
        ### Save to file ###
        if lookup:
            out.write("{};{}\n".format(key,"||".join(Info_list[key])))
        else:
            print("Case 3: {}".format(key))
            break
out.close