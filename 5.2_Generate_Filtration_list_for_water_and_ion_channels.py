# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 10:34:10 2021

@author: dcs839
"""

### Filtration list -- Channels ##

## Import libs ##

import os
import mygene

## Functions ##

mg = mygene.MyGeneInfo()

## Folder and files ##

# Folders #

folder = "Results/Categories/Unfiltrated"

folder_out = "Lists/Filtration lists"

if os.path.exists(folder_out):
    pass
else:
    os.mkdir(folder_out)

# Files #

file1 = "Sample1_FACS_channels_unfiltered.csv"
file2 = "Sample2_PT_channels_unfiltered.csv"
file3 = "Sample3_Male_channels_unfiltered.csv"
file4 = "Sample4_Female_channels_unfiltered.csv"

file_list = [file1,file2,file3,file4]

file_out = "Filtration_list_water_and_ion_channels.csv"

## Global variables ##

Channel_genes = []
Info_list = {}

# read Channel files and get list of genes #

for file in file_list:
    with open(os.path.join(folder,file),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            if not line[0] in Channel_genes:
                Channel_genes.append(line[0])
            else:
                pass
    read.close

### Cellular Component (CC) ##
## Get CC for ensembl entries to use for location filtration ##
with open(os.path.join(folder_out,file_out),'w+',encoding="utf-8") as out:
    out.write("ID;CC\n")
    # initialize counter #
    counter = 0
    for key in Channel_genes:
        ## progress info ##
        counter += 1
        print("{} - {}/{}".format(key,counter,len(Channel_genes)))
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
                if 'CC' in lookup['go']:
                    if lookup['go']['CC']:
                        if not 'term' in lookup['go']['CC']:
                            for item in lookup['go']['CC']:
                                if 'term' in item:
                                    if item['term'].lower() not in Info_list[key]:
                                        Info_list[key].append(item['term'].lower())
                        else:
                            if lookup['go']['CC']['term'].lower() not in Info_list[key]:
                                Info_list[key].append(lookup['go']['CC']['term'].lower())
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