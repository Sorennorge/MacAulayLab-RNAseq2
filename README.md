# MacAulayLab-RNAseq2

The work and scripts are done by the MacAulay Lab.\
All programs used are free and open-source.
In the interest of open science and reproducibility, all data and source code used in our research is provided here.\
Feel free to copy and use code, but make sure to cite: XXXXXXXX (coming soon)\
*Remember* rewrite file_names and folder_names suitable for your pipeline.

## The RNAseq and Analysis follows these steps:
## Raw data analysis - Library Build, Mapping and Quantification ##
The analysis uses RNA STAR for mapping and RSEM for quantification.
### RNA-STAR and RSEM Library build and indexing ###
\
1.1.RNA_STAR_Indexing.sh\
2.1.RSEM_Indexing.sh

### RNA-STAR Mapping and RSEM quantification ###
\
1.2.RNA_STAR_RNAseq2.sh
2.2.RSEM_RNAseq2.sh

## Create count tables with gene information ##
Requirements:\
Biomart of Rnor6.0 with Attributes: Gene stable ID & Gene name\
\
3.1.RSEM_to_count_tables.py

## Transporters and pumps & water and Ion channels ##

### Extract genes of interest ###

4.1_Categories_Transporters_and_pumps
4.2_Categories_water_and_ion_channels

### Filtration for plasma membrane location - gather infomation ###

5.1_Generate_Filtration_list_for_Transporters_and_pumps
5.2_Generate_Filtration_list_for_water_and_ion_channels

### Create filtered list of transporters and channels ###

6.1_Filtration_Transporter_and_pumps
6.2_Filtration_water_and_ion_channels

### Generate Membrane transporer and channel lists ###

7.1_Generate_Membrane_Transporter_category
7.2_Generate_Membrane_Channel_category

