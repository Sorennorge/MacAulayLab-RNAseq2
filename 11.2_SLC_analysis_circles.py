# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 16:45:13 2021

@author: dcs839
"""

### SLC circle analysis ###

## Import packages ##

import os

# Folder #

Folder = "Results/SLC analysis"

# Files #

File1 = "SLC_evaluated.csv"

File2 = "SLC_circle_analysis.csv"

# Global variables #

SLC_groups_concatenated = {}
Group_names = {}

# read file #

with open(os.path.join(Folder, File1),'r') as read:
    for line in read:
        line = line.strip().split(";")
        TPM = float(str(line[3]).replace(",","."))
        if line[4] not in SLC_groups_concatenated:
            SLC_groups_concatenated[line[4]] = [int(line[1]),TPM]
            Group_names[line[4]] = line[5]
        elif line[4] in SLC_groups_concatenated:
            SLC_groups_concatenated[line[4]][0] += int(line[1])
            SLC_groups_concatenated[line[4]][1] += TPM
        else:
            print(line)
            break
read.close

with open(os.path.join(Folder, File2),'w+') as out:
    out.write("Group nr.;Group name; SLCs;TPM (accumulative)\n")
    for key in SLC_groups_concatenated:
        out.write("{};{};{};{}\n".format(key,Group_names[key],SLC_groups_concatenated[key][0],str(round(SLC_groups_concatenated[key][1],2)).replace(".",",")))
out.close