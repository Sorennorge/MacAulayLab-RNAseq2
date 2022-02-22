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

### Count Tables with gene information ###
Requirements:\
Biomart of Rnor6.0 with Attributes: Gene stable ID & Gene name\
\
3.1.RSEM_to_count_tables.py
