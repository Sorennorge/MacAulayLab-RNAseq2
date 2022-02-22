# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 13:19:33 2022

@author: dcs839
"""

### Convert string db edge tables for connection analysis ###

## Input is the edge tables generated from cytoscape with string db plugin ##

## The extracted table only included 'shared_name', 'name', 'display name', and 'query term' ##

## Import packages ##

import os

## Folders ##

Folder = "Results/Network Analysis/lists"

## Files ##

File_1 = "Node_Table_Transporter.csv"
File_2 = "Node_table_Channel.csv"

File_out_1 = "Node_Table_Transporter_clean.csv"
File_out_2 = "Node_table_Channel_clean.csv"

# Global variables #

## Load and write clean files ##

# Transport #

with open(os.path.join(Folder,File_out_1),'w+') as out:
    out.write("String_name;Query_term\n")
    with open(os.path.join(Folder,File_1),'r') as read:
        next(read)
        for line in read:
            line = line.strip().replace('"','').split(",")
            out.write("{};{}\n".format(line[0],line[2]))
    read.close
out.close

# Channel #

with open(os.path.join(Folder,File_out_2),'w+') as out:
    out.write("String_name;Query_term\n")
    with open(os.path.join(Folder,File_2),'r') as read:
        next(read)
        for line in read:
            line = line.strip().replace('"','').split(",")
            out.write("{};{}\n".format(line[0],line[2]))
    read.close
out.close