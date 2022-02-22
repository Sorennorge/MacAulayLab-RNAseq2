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

1.1.RNA_STAR_Indexing.sh \
2.1.RSEM_Indexing.sh

### RNA-STAR Mapping and RSEM quantification ###

1.2.RNA_STAR_RNAseq2.sh \
2.2.RSEM_RNAseq2.sh

## Create count tables with gene information ##
Requirements: \
Biomart of Rnor6.0 with Attributes: Gene stable ID & Gene name 

3.1.RSEM_to_count_tables.py

## Transporters and pumps & water and Ion channels ##

### Extract genes of interest ###

4.1_Categories_Transporters_and_pumps \
4.2_Categories_water_and_ion_channels

### Filtration for plasma membrane location - gather infomation ###
Requirements:\
Targets_and_families list file from https://www.guidetopharmacology.org \
5.1_Generate_Filtration_list_for_Transporters_and_pumps \
5.2_Generate_Filtration_list_for_water_and_ion_channels

### Create filtered list of transporters and channels ###

6.1_Filtration_Transporter_and_pumps \
6.2_Filtration_water_and_ion_channels

### Generate Membrane transporer and channel lists ###

7.1_Generate_Membrane_Transporter_category \
7.2_Generate_Membrane_Channel_category

## Generate other categories of interest ##
We created categories of possible influencers of CSF production.

### G protein-coupled receptors ###
Requirements: \
Targets_and_families list file from https://www.guidetopharmacology.org \
8.1_Generate_GPCRs_category

### Receptor tyrosine kinases ###
Requirements: \
Information gathered from https://www.genenames.org - ‘receptor tyrosine kinase’ including sub group ‘ephrin receptors’ and ‘ErbB family’. \
8.2_Generate_RTKs_category

### Kinases ###
We filtered kinases to only include protein kinases. 
Requirements: \
Information gathered from https://www.genome.jp/kegg - Entries from ‘EC 2.7.10.2’ (non-specific protein-tyrosine kinase), ‘EC 2.7.12’ (Dual-specificity kinases) with the two sub-categories, and ‘EC 2.7.11’ (Protein-serine/threonine kinases) with the 33 sub-categories. \
8.3.1_Generate_Kinases_category \
8.3.2_Generate_Kinases_filtration_list \
8.3.3_Generate_Protein_Kinases 

### Phosphatases ###
We filtered Phosphatases to only include protein Phosphatases. 
Requirements: \
Information gathered from https://www.genome.jp/kegg - Entries from EC 3.1.3 (Phosphoric Monoester Hydrolases) with 108 subcategories. \
8.4.1_Generate_Phosphatases_category \
8.4.2_Generate_Phosphatases_filtration_list \
8.4.3_Generate_Protein_Phosphatases \
8.4.4_Generate_Protein_Phosphatases_from_evaluation \
8.3.4_Generate_Protein_Kinases_from_evaluation 

### Phosphodiesterases ###

8.5_Generate_PDEs_category 

### Cyclases ###
Requirements: \
Information gathered from https://www.genome.jp/kegg - Entries from ‘EC 4.6.1.1’ (adenylate cyclase) and ‘EC 4.6.1.2’ (guanylate cyclase). \
8.6_Generate_Cyclases_category

## Cross species analysis ##

The cross species analysis was created with different count tables excluding mitochondrial RNA from the gtf file in step 1 & 2.

### Create count tables with gene information ###

9.1_Cross_species_RSEM_to_count_tables

### Cross species similarities and plots ###

10.1_Cross_species_analysis_generate_lists \
10.2_Cross_species_analysis \
10.3_Cross_species_analysis_plots \
10.4_Cross_species_analysis_profile_smiliarities

## Solute carrier (SLC) analysis ##

### Transporters and pumps ###

11.1_SLC_analysis \
11.2_SLC_analysis_circles

### Whole choroid plexus ###

11.3_SLC_analysis_whole_CP

## Ranking of tables ##

12.1_Table1_Transporter_table_ranking \
12.2_Table2_Channel_table_ranking \
12.3_Table3_Transporter_table_ranking \
12.4_Table4_Channel_table_ranking

## Comparison of choroid plexus (Male) vs FACS / Female / proximal tubules ##

### Choroid plexus (Male) vs FACS ###

13.1_Comparison_analysis_Male_vs_Facs

### Choroid plexus (Male) vs Female ###

13.2_Comparison_analysis_Male_vs_Female

### Choroid plexus (Male) vs Proximal tubules ###

13.3_Comparison_analysis_Male_vs_PT

## Network analysis ##

### Generate query list for cytoscape and string db plugin ###

14.1_Generate_string_db_entry_list

### Convert node and edge tables for network analysis ###

14.2_Convert_string_db_edge_tables_for_connection_analysis \
14.3_convert_node_and_query_table_for_connection_analysis

### Create tables for network analysis ###

14.3_Create_node_and_egde_tables_for_network_analysis
