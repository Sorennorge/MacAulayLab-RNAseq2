# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 12:11:13 2021

@author: dcs839
"""

### Comparison analysis Male vs PT ###

## Import packages ##

import os
from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt

## output settings ##

# Saved = 0 for show plot, Saved = 1 for save plot #

Saved = 1

### Folders and Files ###

## Folders ##

# Input #
Folder1 = "Lists/Count Tables"
Folder2 = "Results/Supplementary Table/Single sheets"

# Output #
Folder3 = "Results/Comparison"
Folder4 = "Results/Comparison/Figures"

# Create output folder if it doesn't exists #
if os.path.exists(Folder3):
    pass
else:
    os.mkdir(Folder3)
    
if os.path.exists(Folder4):
    pass
else:
    os.mkdir(Folder4)

## Files ##

# Alle genes #
File1 = "Sample3_Male_TPM.csv"
File2 = "Sample2_PT_TPM.csv"

# Transportes #
File3 = "S1_Supplementary Tables.csv"
File4 = "S6_Supplementary Tables.csv"

#Channels #
File5 = "S2_Supplementary Tables.csv"
File6 = "S7_Supplementary Tables.csv"

# Output files #
File_out1 = "Male_vs_PT_all_genes.png"
File_out2 = "Male_vs_PT_Transporters.png"
File_out3 = "Male_vs_PT_Channels.png"

## Global variables ##

Total_Male = []
Total_PT = []

Transporters_Male = []
Transporters_PT = []

Channels_Male = []
Channels_PT = []

## Read count tables ##

with open(os.path.join(Folder1,File1),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            if float(line[3].replace(",",".")) >= 0.5:
                Total_Male.append(line[0])
        else:
            pass
read.close

with open(os.path.join(Folder1,File2),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            if float(line[3].replace(",",".")) >= 0.5:
                Total_PT.append(line[0])
            else:
                pass
        else:
            pass
read.close

## read transporter files ##

with open(os.path.join(Folder2,File3),'r') as read:
    for _ in range(1,4,1):
        next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            if float(line[3].replace(",",".")) >= 0.5:
                Transporters_Male.append(line[0])
        else:
            pass
read.close

with open(os.path.join(Folder2,File4),'r') as read:
    for _ in range(1,4,1):
        next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            if float(line[3].replace(",",".")) >= 0.5:
                Transporters_PT.append(line[0])
            else:
                pass
        else:
            pass
read.close

## read Channel files ##

with open(os.path.join(Folder2,File5),'r') as read:
    for _ in range(1,4,1):
        next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            if float(line[3].replace(",",".")) >= 0.5:
                Channels_Male.append(line[0])
        else:
            pass
read.close

with open(os.path.join(Folder2,File6),'r') as read:
    for _ in range(1,4,1):
        next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            if float(line[3].replace(",",".")) >= 0.5:
                Channels_PT.append(line[0])
            else:
                pass
        else:
            pass
read.close


### Male vs PT - all genes ###
total = len(set(Total_Male).union(set(Total_PT)))
venn_diagram = venn2([set(Total_Male), set(Total_PT)],set_labels = ('Male', 'PT'),set_colors=("#009900", "#660066"),alpha=0.55,subset_label_formatter=lambda x: str(x) + "\n(" + f"{(x/total):1.0%}" + ")")
#colors
venn_diagram.get_patch_by_id('10').set_color("#3366FF") #CP
venn_diagram.get_patch_by_id('01').set_color("#663300") #PT
venn_diagram.get_patch_by_id('11').set_color("#4D4D80") #Shared
venn_diagram.get_patch_by_id('10').set_edgecolor('none') #CP
venn_diagram.get_patch_by_id('01').set_edgecolor('none') #PT
venn_diagram.get_patch_by_id('11').set_edgecolor('none') #Shared

#labels
venn_diagram.get_label_by_id("100").set_x(-0.75)
venn_diagram.get_label_by_id("010").set_x(0.66)
venn_diagram.get_label_by_id("A").set_x(-0.4)
venn_diagram.get_label_by_id("A").set_y(-0.5)
venn_diagram.get_label_by_id("B").set_x(0.35)
venn_diagram.get_label_by_id("B").set_y(-0.5)
plt.title('Common male and PT genes > 0.5 TPM',fontname="Times New Roman",fontweight="bold",fontsize=20, pad=30,color="black",style="italic")
for text in venn_diagram.set_labels:
    text.set_fontsize(20)
    text.set_family("Times New Roman")
for text in venn_diagram.subset_labels:
    text.set_fontsize(15)
    text.set_family("Times New Roman")
venn_diagram.get_label_by_id("110").set_fontsize(25)
if Saved == 1:
    plt.savefig(os.path.join(Folder4,File_out1),dpi=600,bbox_inches='tight')
    plt.close()
else:
    plt.show()

### Male vs PT - Transporters ###
total = len(set(Transporters_Male).union(set(Transporters_PT)))
venn_diagram = venn2([set(Transporters_Male), set(Transporters_PT)],set_labels = ('Male', 'PT'),set_colors=("#009900", "#660066"),alpha=0.55,subset_label_formatter=lambda x: str(x) + "\n(" + f"{(x/total):1.0%}" + ")")
#colors
venn_diagram.get_patch_by_id('10').set_color("#3366FF") #CP
venn_diagram.get_patch_by_id('01').set_color("#663300") #PT
venn_diagram.get_patch_by_id('11').set_color("#4D4D80") #Shared
venn_diagram.get_patch_by_id('10').set_edgecolor('none') #CP
venn_diagram.get_patch_by_id('01').set_edgecolor('none') #PT
venn_diagram.get_patch_by_id('11').set_edgecolor('none') #Shared

#labels
venn_diagram.get_label_by_id("100").set_x(-0.75)
venn_diagram.get_label_by_id("010").set_x(0.75)
venn_diagram.get_label_by_id("A").set_x(-0.4)
venn_diagram.get_label_by_id("A").set_y(-0.5)
venn_diagram.get_label_by_id("B").set_x(0.35)
venn_diagram.get_label_by_id("B").set_y(-0.5)
plt.title('Common male and PT Transporter genes > 0.5 TPM',fontname="Times New Roman",fontweight="bold",fontsize=20, pad=30,color="black",style="italic")
for text in venn_diagram.set_labels:
    text.set_fontsize(20)
    text.set_family("Times New Roman")
for text in venn_diagram.subset_labels:
    text.set_fontsize(15)
    text.set_family("Times New Roman")
venn_diagram.get_label_by_id("110").set_fontsize(25)
if Saved == 1:
    plt.savefig(os.path.join(Folder4,File_out2),dpi=600,bbox_inches='tight')
    plt.close()
else:
    plt.show()
    
### Male vs PT - Channels ###
total = len(set(Channels_Male).union(set(Channels_PT)))
venn_diagram = venn2([set(Channels_Male), set(Channels_PT)],set_labels = ('Male', 'PT'),set_colors=("#009900", "#660066"),alpha=0.55,subset_label_formatter=lambda x: str(x) + "\n(" + f"{(x/total):1.0%}" + ")")
#colors
venn_diagram.get_patch_by_id('10').set_color("#3366FF") #CP
venn_diagram.get_patch_by_id('01').set_color("#663300") #PT
venn_diagram.get_patch_by_id('11').set_color("#4D4D80") #Shared
venn_diagram.get_patch_by_id('10').set_edgecolor('none') #CP
venn_diagram.get_patch_by_id('01').set_edgecolor('none') #PT
venn_diagram.get_patch_by_id('11').set_edgecolor('none') #Shared

#labels
venn_diagram.get_label_by_id("100").set_x(-0.75)
venn_diagram.get_label_by_id("010").set_x(0.75)
venn_diagram.get_label_by_id("A").set_x(-0.4)
venn_diagram.get_label_by_id("A").set_y(-0.5)
venn_diagram.get_label_by_id("B").set_x(0.35)
venn_diagram.get_label_by_id("B").set_y(-0.5)
plt.title('Common male and PT Channel genes > 0.5 TPM',fontname="Times New Roman",fontweight="bold",fontsize=20, pad=30,color="black",style="italic")
for text in venn_diagram.set_labels:
    text.set_fontsize(20)
    text.set_family("Times New Roman")
for text in venn_diagram.subset_labels:
    text.set_fontsize(15)
    text.set_family("Times New Roman")
venn_diagram.get_label_by_id("110").set_fontsize(25)
if Saved == 1:
    plt.savefig(os.path.join(Folder4,File_out3),dpi=600,bbox_inches='tight')
    plt.close()
else:
    plt.show()