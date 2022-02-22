# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 13:48:37 2022

@author: dcs839
"""

### Create node and edge tables for network analysis ###

## import packages ###

import os

## Folders ###

Folder_1 = "Results/Supplementary Table/Single sheets"
Folder_2 = "Results/Network Analysis/lists"
Folder_3 = "Results/Network Analysis/lists/Procced"

if os.path.exists(Folder_2):
    pass
else:
    os.mkdir(Folder_2)

## Files ##
    
File_1 = "Node_Table_Transporter_clean.csv"
File_2 = "Node_table_Channel_clean.csv"

File_3 = "Edge_table_transporter_clean.csv"
File_4 = "Edge_Table_channels_clean.csv"


File_out_1 = "Node_Table_Transporter_Network_analysis.csv"
File_out_2 = "Node_table_Channel_Network_analysis.csv"

File_out_3 = "Edge_table_transporter_Network_analysis.csv"
File_out_4 = "Edge_Table_channels_Network_analysis.csv"

# Category files #

file1 = "S1_Supplementary_Tables_2021_12_29.csv" #Transporters
file2 = "S2_Supplementary_Tables_2021_12_29.csv" #Channels
file3 = "S8_Supplementary_Tables_2021_12_29.csv" #GPCRs
file4 = "S9_Supplementary_Tables_2021_12_29.csv" #RTKs
file5 = "S10_Supplementary_Tables_2021_12_29.csv" #Kinases
file6 = "S11_Supplementary_Tables_2021_12_29.csv" #Phosphatases
file7 = "S12_Supplementary_Tables_2021_12_29.csv" #PDEs
file8 = "S13_Supplementary_Tables_2021_12_29.csv" #Cyclases

category_file_list = [file1,file2,file3,file4,file5,file6,file7,file8]

### Global varibales ###

Category_dict = {}
Node_table_info_dict = {}
Query_term_to_ensembl = {}
Transport_node_table = {}
Channel_node_table = {}
Transport_edge_table = []
Channel_edge_table = []

# If another cutoff is needed change these #
Edge_transport_cutoff = 0.6
Edge_channel_cutoff = 0.7

Node_table_Header = "Ensemble ID;Gene;Alias;TPM;Category\n"
Edge_table_Header = "Source;interaction;Target;string_score\n"

Correct_Transport_edge_table= []
Correct_Channel_edge_table = []

### Read files ###

## Category files ##
for i in range(0,8,1):
    with open(os.path.join(Folder_1,category_file_list[i]),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            Node_table_info_dict[line[0]] = line[1:4]
            Query_term_to_ensembl[line[1]] = line[0]
            if not line[0] == '' and i == 0:
                Category_dict[line[0]] = 'Transporter'
            elif not line[0] == '' and i == 1:
                Category_dict[line[0]] = 'Channels'
            elif not line[0] == '' and i == 2:
                Category_dict[line[0]] = 'GPCRs'
            elif not line[0] == '' and i == 3:
                Category_dict[line[0]] = 'RTKs'
            elif not line[0] == '' and i == 4:
                Category_dict[line[0]] = 'Kinases'
            elif not line[0] == '' and i == 5:
                Category_dict[line[0]] = 'Phosphatases'
            elif not line[0] == '' and i == 6:
                Category_dict[line[0]] = 'PDEs'
            elif not line[0] == '' and i == 7:
                Category_dict[line[0]] = 'Cyclases'
    read.close

## Node table ##

# Transport #

with open(os.path.join(Folder_2,File_1),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        Transport_node_table[line[0]] = Query_term_to_ensembl[line[1]]
read.close

# Channel #

with open(os.path.join(Folder_2,File_2),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        Channel_node_table[line[0]] = Query_term_to_ensembl[line[1]]
read.close

## Edge table ##

# Transport #

with open(os.path.join(Folder_2,File_3),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if float(line[2]) >= Edge_transport_cutoff:
            if not line[4] == '' or not line[5] == '':
                Transport_edge_table.append([Transport_node_table[line[0]],Transport_node_table[line[1]],line[2]])
            else:
                pass
        else:
            pass
read.close

# Channels #
with open(os.path.join(Folder_2,File_4),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if float(line[2]) >= Edge_channel_cutoff:
            if not line[4] == '' or not line[5] == '':
                Channel_edge_table.append([Channel_node_table[line[0]],Channel_node_table[line[1]],line[2]])
            else:
                pass
        else:
            pass
read.close

### Only get connections between transporter / channels and regulation ###

for key in Transport_edge_table:
    if Category_dict[key[0]] == 'Transporter' or Category_dict[key[1]] == 'Transporter':
        if not Category_dict[key[0]] == Category_dict[key[1]]:
            Correct_Transport_edge_table.append(key)
        else:
            pass
    else:
        pass

for key in Channel_edge_table:
    if Category_dict[key[0]] == 'Channels' or Category_dict[key[1]] == 'Channels':
        if not Category_dict[key[0]] == Category_dict[key[1]]:
            Correct_Channel_edge_table.append(key)
        else:
            pass
    else:
        pass


### Print correct node and edge tables for network analysis ###

# Transport - Node #
with open(os.path.join(Folder_3,File_out_1),'w+') as out:
    out.write(Node_table_Header)
    for key in Transport_node_table:
        identifier = Transport_node_table[key]
        out.write("{};{};{};{};{}\n".format(identifier,Node_table_info_dict[identifier][0],Node_table_info_dict[identifier][1],Node_table_info_dict[identifier][2],Category_dict[identifier]))
out.close

# Channel - Node #
with open(os.path.join(Folder_3,File_out_2),'w+') as out:
    out.write(Node_table_Header)
    for key in Channel_node_table:
        identifier = Channel_node_table[key]
        out.write("{};{};{};{};{}\n".format(identifier,Node_table_info_dict[identifier][0],Node_table_info_dict[identifier][1],Node_table_info_dict[identifier][2],Category_dict[identifier]))
out.close

# Transport - Edge #

with open(os.path.join(Folder_3,File_out_3),'w+') as out:
    out.write(Edge_table_Header)
    for key in Correct_Transport_edge_table:
        out.write("{};pp;{};{}\n".format(key[0],key[1],key[2]))
out.close

# Channel - Edge #
with open(os.path.join(Folder_3,File_out_4),'w+') as out:
    out.write(Edge_table_Header)
    for key in Correct_Channel_edge_table:
        out.write("{};pp;{};{}\n".format(key[0],key[1],key[2]))
out.close
