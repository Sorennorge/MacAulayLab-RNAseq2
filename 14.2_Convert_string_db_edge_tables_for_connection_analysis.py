# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 16:18:45 2021

@author: dcs839
"""

### Convert string db edge tables for connection analysis ###

## Input is the edge tables generated from cytoscape with string db plugin ##

## Import packages ##

import os

## Folders ##

Folder = "Results/Network Analysis/lists"

## Files ##

File_1 = "Edge_table_transporter.csv"
File_2 = "Edge_Table_channels.csv"


File_out_1 = "Edge_table_transporter_clean.csv"
File_out_2 = "Edge_Table_channels_clean.csv"

## Load and write clean files ##

# Transport #

with open(os.path.join(Folder,File_out_1),'w+') as out:
    out.write("PP1;PP2;score;textmining;experiments;databases;co-expression;neighborhood;gene fusion;co-occurrence;interspecies\n")
    with open(os.path.join(Folder,File_1),'r') as read:
        next(read)
        for line in read:
            line = line.strip().replace('"','').replace('stringdb::','').split(",")
            inter_proteins = (line[1].split(" (pp) "))
            data = [line[12],line[13],line[8],line[7],line[5],line[11],line[9],line[6],line[10]]
            out.write("{};{}\n".format(";".join(inter_proteins),";".join(data)))
    read.close
out.close

# Channels #

with open(os.path.join(Folder,File_out_2),'w+') as out:
    out.write("PP1;PP2;score;textmining;experiments;databases;co-expression;neighborhood;gene fusion;co-occurrence;interspecies\n")
    with open(os.path.join(Folder,File_2),'r') as read:
        next(read)
        for line in read:
            line = line.strip().replace('"','').replace('stringdb::','').split(",")
            inter_proteins = (line[1].split(" (pp) "))
            data = [line[12],line[13],line[8],line[7],line[5],line[11],line[9],line[6],line[10]]
            out.write("{};{}\n".format(";".join(inter_proteins),";".join(data)))
    read.close
out.close