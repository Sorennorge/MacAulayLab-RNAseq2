# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 14:53:18 2021

@author: dcs839
"""

### string db - entry list ###

## Import packages ##

import os

### Folders and Files ###

## Folders ##

folder1 = "Results/Supplementary Table/Single sheets"
folder_out1 = "Results/Network Analysis"
folder_out2 = "Results/Network Analysis/lists"

if os.path.exists(folder_out1):
    pass
else:
    os.mkdir(folder_out1)

if os.path.exists(folder_out2):
    pass
else:
    os.mkdir(folder_out2)

## Files ##

file1 = "S1_Supplementary_Tables.csv" #Transporters
file2 = "S2_Supplementary_Tables.csv" #Channels
file3 = "S8_Supplementary_Tables.csv" #GPCRs
file4 = "S9_Supplementary_Tables.csv" #RTKs
file5 = "S10_Supplementary_Tables.csv" #Kinases
file6 = "S11_Supplementary_Tables.csv" #Phosphatases
file7 = "S12_Supplementary_Tables.csv" #PDEs
file8 = "S13_Supplementary_Tables.csv" #Cyclases

file_out1 = "Transport_oriented_list_for_network_analysis.csv"
file_out2 = "Channel_oriented_list_for_network_analysis.csv"

## Global variables ##

# Single category #
Transporters_list = []
Channel_list = []
GPCR_list = []
RTK_list = []
Kinase_list = []
Phosphatase_list = []
PDE_list = []
Cyclase_list = []

# Collection #

Collection_list_of_lists_tranporsters = [Transporters_list, GPCR_list, RTK_list, Kinase_list, Phosphatase_list, PDE_list, Cyclase_list]
Collection_list_of_lists_channels = [Channel_list, GPCR_list, RTK_list, Kinase_list, Phosphatase_list, PDE_list, Cyclase_list]

Transporter_collection_list = []
Channel_collection_list = []

# Transport #

with open(os.path.join(folder1,file1),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[1] == '':
            Transporters_list.append(line[1])
        else:
            pass
read.close

# Channels #

with open(os.path.join(folder1,file2),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[1] == '':
            Channel_list.append(line[1])
        else:
            pass
read.close

# GPCRs #

with open(os.path.join(folder1,file3),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[1] == '':
            GPCR_list.append(line[1])
        else:
            pass
read.close

# RTKs #

with open(os.path.join(folder1,file4),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[1] == '':
            RTK_list.append(line[1])
        else:
            pass
read.close

# Kinases #

with open(os.path.join(folder1,file5),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[1] == '':
            Kinase_list.append(line[1])
        else:
            pass
read.close

# Phosphatases #

with open(os.path.join(folder1,file6),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[1] == '':
            Phosphatase_list.append(line[1])
        else:
            pass
read.close

# PDEs #

with open(os.path.join(folder1,file7),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[1] == '':
            PDE_list.append(line[1])
        else:
            pass
read.close

# Cyclases #

with open(os.path.join(folder1,file8),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[1] == '':
            Cyclase_list.append(line[1])
        else:
            pass
read.close

## Generate collection lists ##

# Transporters #

for key in Collection_list_of_lists_tranporsters:
    for item in key:
        if item not in Transporter_collection_list:
            Transporter_collection_list.append(item)
        else:
            print(item)
            break

# Channels #

for key in Collection_list_of_lists_channels:
    for item in key:
        if item not in Channel_collection_list:
            Channel_collection_list.append(item)
        else:
            print(item)
            break
with open(os.path.join(folder_out2,file_out1),'w+') as out:
    for key in Transporter_collection_list:
        out.write("{}\n".format(key))
out.close

## Save lists to files ##
with open(os.path.join(folder_out2,file_out1),'w+') as out:
    for key in Transporter_collection_list:
        out.write("{}\n".format(key))
out.close

with open(os.path.join(folder_out2,file_out2),'w+') as out:
    for key in Channel_collection_list:
        out.write("{}\n".format(key))
out.close