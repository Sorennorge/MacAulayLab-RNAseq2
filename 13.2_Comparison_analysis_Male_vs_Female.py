# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 12:19:57 2021

@author: dcs839
"""

### Comparison analysis Male vs Female ###

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
Folder3 = "Results/Categories/1.Transporter and pumps/Manual Filtration/Evaluated"
Folder4 = "Results/Categories/2.Water and ion Channels/Manual Filtration/Evaluated"

# Output #
Folder_out1 = "Results/Comparison"
Folder_out2 = "Results/Comparison/Figures"

# Create output folder if it doesn't exists #
if os.path.exists(Folder_out1):
    pass
else:
    os.mkdir(Folder_out1)
    
if os.path.exists(Folder_out2):
    pass
else:
    os.mkdir(Folder_out2)

## Files ##

# Alle genes #
File1 = "Sample3_Male_TPM.csv"
File2 = "Sample4_Female_TPM.csv"

# Transportes #
File3 = "S1_Supplementary Tables.csv"
File4 = "Sample4_Manual_filtration_Female_Membrane_Transporter_and_pumps_evaluated.csv"

#Channels #
File5 = "S2_Supplementary Tables.csv"
File6 = "Sample4_Manual_filtration_Female_Membrane_Water_and_ion_channels_evaluated.csv"

# Output files #
File_out1 = "Male_vs_Female_all_genes.png"
File_out2 = "Male_vs_Female_Transporters.png"
File_out3 = "Male_vs_Female_Channels.png"

## Global variables ##

Total_Male = []
Total_Female = []

Transporters_Male = []
Transporters_Female = []

Channels_Male = []
Channels_Female = []

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
                Total_Female.append(line[0])
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

with open(os.path.join(Folder3,File4),'r') as read:
    for _ in range(1,4,1):
        next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            if float(line[2].replace(",",".")) >= 0.5:
                Transporters_Female.append(line[0])
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

with open(os.path.join(Folder4,File6),'r') as read:
    for _ in range(1,4,1):
        next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            if float(line[2].replace(",",".")) >= 0.5:
                Channels_Female.append(line[0])
            else:
                pass
        else:
            pass
read.close


### Male vs Female - all genes ###
total = len(set(Total_Male).union(set(Total_Female)))
venn_diagram = venn2([set(Total_Male), set(Total_Female)],set_labels = ('Male', 'Female'),set_colors=("#009900", "#660066"),alpha=0.55,subset_label_formatter=lambda x: str(x) + "\n(" + f"{(x/total):1.0%}" + ")")
#colors
venn_diagram.get_patch_by_id('10').set_color("#3366FF") #CP
venn_diagram.get_patch_by_id('01').set_color("#FF66FF") #Female
venn_diagram.get_patch_by_id('11').set_color("#9966FF") #Shared
venn_diagram.get_patch_by_id('10').set_edgecolor('none') #Rat
venn_diagram.get_patch_by_id('01').set_edgecolor('none') #Female
venn_diagram.get_patch_by_id('11').set_edgecolor('none') #Shared

#labels
venn_diagram.get_label_by_id("100").set_x(-0.75)
venn_diagram.get_label_by_id("010").set_x(0.66)
venn_diagram.get_label_by_id("A").set_x(-0.4)
venn_diagram.get_label_by_id("A").set_y(-0.5)
venn_diagram.get_label_by_id("B").set_x(0.35)
venn_diagram.get_label_by_id("B").set_y(-0.5)
plt.title('Common male and Female genes > 0.5 TPM',fontname="Times New Roman",fontweight="bold",fontsize=20, pad=30,color="black",style="italic")
for text in venn_diagram.set_labels:
    text.set_fontsize(20)
    text.set_family("Times New Roman")
for text in venn_diagram.subset_labels:
    text.set_fontsize(15)
    text.set_family("Times New Roman")
venn_diagram.get_label_by_id("110").set_fontsize(25)
if Saved == 1:
    plt.savefig(os.path.join(Folder_out2,File_out1),dpi=600,bbox_inches='tight')
    plt.close()
else:
    plt.show()

### Male vs Female - Transporters ###
total = len(set(Transporters_Male).union(set(Transporters_Female)))
venn_diagram = venn2([set(Transporters_Male), set(Transporters_Female)],set_labels = ('Male', 'Female'),set_colors=("#009900", "#660066"),alpha=0.55,subset_label_formatter=lambda x: str(x) + "\n(" + f"{(x/total):1.0%}" + ")")
#colors
venn_diagram.get_patch_by_id('10').set_color("#3366FF") #CP
venn_diagram.get_patch_by_id('01').set_color("#FF66FF") #Female
venn_diagram.get_patch_by_id('11').set_color("#9966FF") #Shared
venn_diagram.get_patch_by_id('10').set_edgecolor('none') #Rat
venn_diagram.get_patch_by_id('01').set_edgecolor('none') #Female
venn_diagram.get_patch_by_id('11').set_edgecolor('none') #Shared

#labels
venn_diagram.get_label_by_id("100").set_x(-0.75)
venn_diagram.get_label_by_id("010").set_x(0.66)
venn_diagram.get_label_by_id("A").set_x(-0.4)
venn_diagram.get_label_by_id("A").set_y(-0.5)
venn_diagram.get_label_by_id("B").set_x(0.35)
venn_diagram.get_label_by_id("B").set_y(-0.5)
plt.title('Common male and Female Transporter genes > 0.5 TPM',fontname="Times New Roman",fontweight="bold",fontsize=20, pad=30,color="black",style="italic")
for text in venn_diagram.set_labels:
    text.set_fontsize(20)
    text.set_family("Times New Roman")
for text in venn_diagram.subset_labels:
    text.set_fontsize(15)
    text.set_family("Times New Roman")
venn_diagram.get_label_by_id("110").set_fontsize(25)
if Saved == 1:
    plt.savefig(os.path.join(Folder_out2,File_out2),dpi=600,bbox_inches='tight')
    plt.close()
else:
    plt.show()
    
### Male vs Female - Channels ###
total = len(set(Channels_Male).union(set(Channels_Female)))
venn_diagram = venn2([set(Channels_Male), set(Channels_Female)],set_labels = ('Male', 'Female'),set_colors=("#009900", "#660066"),alpha=0.55,subset_label_formatter=lambda x: str(x) + "\n(" + f"{(x/total):1.0%}" + ")")
#colors
venn_diagram.get_patch_by_id('10').set_color("#3366FF") #CP
venn_diagram.get_patch_by_id('01').set_color("#FF66FF") #Female
venn_diagram.get_patch_by_id('11').set_color("#9966FF") #Shared
venn_diagram.get_patch_by_id('10').set_edgecolor('none') #Rat
venn_diagram.get_patch_by_id('01').set_edgecolor('none') #Female
venn_diagram.get_patch_by_id('11').set_edgecolor('none') #Shared

#labels
venn_diagram.get_label_by_id("100").set_x(-0.75)
venn_diagram.get_label_by_id("010").set_x(0.66)
venn_diagram.get_label_by_id("A").set_x(-0.4)
venn_diagram.get_label_by_id("A").set_y(-0.5)
venn_diagram.get_label_by_id("B").set_x(0.35)
venn_diagram.get_label_by_id("B").set_y(-0.5)
plt.title('Common male and Female Channel genes > 0.5 TPM',fontname="Times New Roman",fontweight="bold",fontsize=20, pad=30,color="black",style="italic")
for text in venn_diagram.set_labels:
    text.set_fontsize(20)
    text.set_family("Times New Roman")
for text in venn_diagram.subset_labels:
    text.set_fontsize(15)
    text.set_family("Times New Roman")
venn_diagram.get_label_by_id("110").set_fontsize(25)
if Saved == 1:
    plt.savefig(os.path.join(Folder_out2,File_out3),dpi=600,bbox_inches='tight')
    plt.close()
else:
    plt.show()
