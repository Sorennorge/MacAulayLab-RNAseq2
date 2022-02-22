# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:04:13 2021

@author: dcs839
"""

### Plot figures for cross species ###

## Import libs ##

import os
from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt

### out setup ###

# Saved = 0 for show plot, Saved = 1 for save plot #

Saved = 1

### Folder and Files ###

## Folders ##

folder1 = "lists/Count Tables/Cross species/Rat"
folder2 = "Results/Cross species"
folder3 = "Results/Cross species/Figures"

if os.path.exists(folder3):
    pass
else:
    os.mkdir(folder3)

## Files ##

Rat_file = "CS_Rat_TPM.csv"
Human_file = "Human_shared_rat_protein_coding_genes.csv"
Mouse_file = "Mouse_shared_rat_protein_coding_genes.csv"

## Global variables ##

Rat_genes_list = []
Human_genes_list = []
Mouse_genes_list = []

## Read files ##

# Rat #
with open(os.path.join(folder1,Rat_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if not line[0] == '':
            Rat_genes_list.append(line[0])
read.close

# Human #
with open(os.path.join(folder2,Human_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip()
        if not line == '':
            Human_genes_list.append(line)
read.close

# Mouse #
with open(os.path.join(folder2,Mouse_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip()
        if not line == '':
            Mouse_genes_list.append(line)
read.close


### Human vs Rat ###
total = len(set(Rat_genes_list))
venn_diagram = venn2([set(Rat_genes_list), set(Human_genes_list)],set_labels = ('Rat', 'Human'),set_colors=("#88c7dc", "#7ecfd4"),alpha=0.55,subset_label_formatter=lambda x: str(x) + "\n(" + f"{(x/total):1.0%}" + ")")
#colors
venn_diagram.get_patch_by_id('10').set_color("#3366FF") #Rat
venn_diagram.get_patch_by_id('01').set_color("#66CC66") #Human
venn_diagram.get_patch_by_id('11').set_color("#4D99B3") #Shared
venn_diagram.get_patch_by_id('10').set_edgecolor('none') #Rat
venn_diagram.get_patch_by_id('01').set_edgecolor('none') #Human
venn_diagram.get_patch_by_id('11').set_edgecolor('none') #Shared

#labels
venn_diagram.get_label_by_id("100").set_x(-0.68)
venn_diagram.get_label_by_id("010").set_x(0.72)
venn_diagram.get_label_by_id("A").set_x(-0.4)
venn_diagram.get_label_by_id("A").set_y(-0.5)
venn_diagram.get_label_by_id("B").set_x(0.35)
venn_diagram.get_label_by_id("B").set_y(-0.5)
plt.title('Common protein coding genes',fontname="Times New Roman",fontweight="bold",fontsize=20, pad=30,color="black",style="italic")
for text in venn_diagram.set_labels:
    text.set_fontsize(20)
    text.set_family("Times New Roman")
for text in venn_diagram.subset_labels:
    text.set_fontsize(15)
    text.set_family("Times New Roman")
venn_diagram.get_label_by_id("110").set_fontsize(25)
venn_diagram.get_label_by_id("110").set_fontsize(25)
if Saved == 1:
    plt.savefig(os.path.join(folder3,"Rat_vs_Human.png"),dpi=600,bbox_inches='tight')
    plt.close()
else:
    plt.show()


### Mouse vs Rat ### 
venn_diagram = venn2([set(Rat_genes_list), set(Mouse_genes_list)],set_labels = ('Rat', 'Mouse'),set_colors=("#88c7dc", "#3c89d0"),alpha=0.55,subset_label_formatter=lambda x: str(x) + "\n(" + f"{(x/total):1.0%}" + ")")
#colors
venn_diagram.get_patch_by_id('10').set_color("#3366FF") #Rat
venn_diagram.get_patch_by_id('01').set_color("#000066") #Mouse
venn_diagram.get_patch_by_id('11').set_color("#1A33B3") #Shared
venn_diagram.get_patch_by_id('10').set_edgecolor('none') #Rat
venn_diagram.get_patch_by_id('01').set_edgecolor('none') #Mouse
venn_diagram.get_patch_by_id('11').set_edgecolor('none') #Shared

#labels
venn_diagram.get_label_by_id("100").set_x(-0.72)
venn_diagram.get_label_by_id("010").set_x(0.72)
venn_diagram.get_label_by_id("A").set_x(-0.4)
venn_diagram.get_label_by_id("A").set_y(-0.5)
venn_diagram.get_label_by_id("B").set_x(0.35)
venn_diagram.get_label_by_id("B").set_y(-0.5)
plt.title('Common protein coding genes',fontname="Times New Roman",fontweight="bold",fontsize=20, pad=30,color="black",style="italic")
for text in venn_diagram.set_labels:
    text.set_fontsize(20)
    text.set_family("Times New Roman")
for text in venn_diagram.subset_labels:
    text.set_fontsize(15)
    text.set_family("Times New Roman")
venn_diagram.get_label_by_id("110").set_fontsize(25)
venn_diagram.get_label_by_id("110").set_fontsize(25)
if Saved == 1:
    plt.savefig(os.path.join(folder3,"Rat_vs_Mouse.png"),dpi=600,bbox_inches='tight')
    plt.close()
else:
    plt.show()
