# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 08:38:58 2021

@author: dcs839
"""

### Rsem to count tables ###

## Import libs ##

import os

### Folder and Files ###

## Folders ##
folder = "Lists"
folder1 = folder+"/Samples/Sample1"
folder2 = folder+"/Samples/Sample2"
folder3 = folder+"/Samples/Sample3"
folder4 = folder+"/Samples/Sample4"

folder_out = folder+"/Count Tables"

# if output folder doesn't exists, make one
if os.path.exists(folder_out):
    pass
else:
    os.mkdir(folder_out)

## Files ##

# Rnor6.0 with Gene stable ID & Gene name #

file_biomart = "Rat_biomart.txt" 

# Files from step 1 & 2 #

file1 = "Sample1.rsem.genes"
file2 = "Sample2.rsem.genes"
file3 = "Sample3.rsem.genes"
file4 = "Sample4.rsem.genes"

file1_out = "Sample1_FACS_TPM.csv"
file2_out = "Sample2_PT_TPM.csv"
file3_out = "Sample3_Male_TPM.csv"
file4_out = "Sample4_Female_TPM.csv"

## Variables ##

biomart = {}

sample1_rsem_gene_ids = {}
sample2_rsem_gene_ids = {}
sample3_rsem_gene_ids = {}
sample4_rsem_gene_ids = {}

### Read files ###

## Read biomart ##
with open(os.path.join(folder,file_biomart),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(",")
        #check if there is dublicates of Ensembl stable gene ids to gene conversion
        if line[0] in biomart:
            #if same, just pass
            if biomart[line[0]] == line[8].upper():
                pass
            else:
                #if not the same, print the scoundrel and break.
                print(line[0],biomart[line[0]],line[8])
                break
        else:
            #if not in dict, add to dict
            biomart[line[0]] = line[8].upper()
read.close

### for each sample ###
## Sample 1 - FACS ##

with open(os.path.join(folder1,file1),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split("\t")
        #if TPM > 0, add to dict
        if float(line[5]) > 0:
            # Make sure there isnt dublicates
            if not line[0] in sample1_rsem_gene_ids:
                sample1_rsem_gene_ids[line[0]] = line[1:]
            else:
                print(line[0])
                break
read.close

## Sample 2 - Proximal tubules ##

with open(os.path.join(folder2,file2),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split("\t")
        #if TPM > 0, add to dict
        if float(line[5]) > 0:
            # Make sure there isnt dublicates
            if not line[0] in sample2_rsem_gene_ids:
                sample2_rsem_gene_ids[line[0]] = line[1:]
            else:
                print(line[0])
                break
read.close

## Sample 3 - Male ##

with open(os.path.join(folder3,file3),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split("\t")
        #if TPM > 0, add to dict
        if float(line[5]) > 0:
            if not line[0] in sample3_rsem_gene_ids:
                sample3_rsem_gene_ids[line[0]] = line[1:]
            else:
                print(line[0])
                break
read.close

## Sample 4 - Female ##

with open(os.path.join(folder4,file4),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split("\t")
        #if TPM > 0, add to dict
        if float(line[5]) > 0:
            if not line[0] in sample4_rsem_gene_ids:
                sample4_rsem_gene_ids[line[0]] = line[1:]
            else:
                print(line[0])
                break
read.close

### Save count tables to files ###
## Sample 1 - FACS ##

with open(os.path.join(folder_out,file1_out),'w+') as out:
    #Add header
    out.write("Ensembl gene id;Ensembl transcripts;Gene Symbol;TPM\n")
    for key in sample1_rsem_gene_ids:
        if biomart[key] == '':
            out.write("{};{};Missing information;{}\n".format(key,sample1_rsem_gene_ids[key][0],sample1_rsem_gene_ids[key][4].replace(".",",")))
        else:
            out.write("{};{};{};{}\n".format(key,sample1_rsem_gene_ids[key][0],biomart[key],sample1_rsem_gene_ids[key][4].replace(".",",")))
out.close

## Sample 2 - Proximal tubules ##

with open(os.path.join(folder_out,file2_out),'w+') as out:
    #Add header
    out.write("Ensembl gene id;Ensembl transcripts;Gene Symbol;TPM\n")
    for key in sample2_rsem_gene_ids:
        if biomart[key] == '':
            out.write("{};{};Missing information;{}\n".format(key,sample2_rsem_gene_ids[key][0],sample2_rsem_gene_ids[key][4].replace(".",",")))
        else:
            out.write("{};{};{};{}\n".format(key,sample2_rsem_gene_ids[key][0],biomart[key],sample2_rsem_gene_ids[key][4].replace(".",",")))
out.close

## Sample 3 - Male ##

with open(os.path.join(folder_out,file3_out),'w+') as out:
    #Add header
    out.write("Ensembl gene id;Ensembl transcripts;Gene Symbol;TPM\n")
    for key in sample3_rsem_gene_ids:
        if biomart[key] == '':
            out.write("{};{};Missing information;{}\n".format(key,sample3_rsem_gene_ids[key][0],sample3_rsem_gene_ids[key][4].replace(".",",")))
        else:
            out.write("{};{};{};{}\n".format(key,sample3_rsem_gene_ids[key][0],biomart[key],sample3_rsem_gene_ids[key][4].replace(".",",")))
out.close

## Sample 4 - Female ##

with open(os.path.join(folder_out,file4_out),'w+') as out:
    #Add header
    out.write("Ensembl gene id;Ensembl transcripts;Gene Symbol;TPM\n")
    for key in sample4_rsem_gene_ids:
        if biomart[key] == '':
            out.write("{};{};Missing information;{}\n".format(key,sample4_rsem_gene_ids[key][0],sample4_rsem_gene_ids[key][4].replace(".",",")))
        else:
            out.write("{};{};{};{}\n".format(key,sample4_rsem_gene_ids[key][0],biomart[key],sample4_rsem_gene_ids[key][4].replace(".",",")))
out.close