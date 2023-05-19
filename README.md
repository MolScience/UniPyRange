# UniPyRange
Tool to fetch protein/DNA truncation constructs from Uniprot DB

Very simple python script which saves you the pains of counting the amino acids/DNA bases in fasta files from the Uniprot and NCBI RefSeq Database (1, 2).
Lets say you want the amino acid sequence of range 128-387 from a 1000 amino acid protein - this script will help you to avoid counting mistakes by just showing you the specified sequence in amino acids and coding DNA base pairs (ideal for amplification primer design) of a specified Uniprot ID.

![image](https://github.com/MolScience/UniPyRange/assets/134095202/2fea94a3-ba9d-4ab5-a764-d50c196ba1d1)


- Requires BioPython (3) and Bioservices Package (4)


(1)
The UniProt Consortium
UniProt: a hub for protein information
Nucleic Acids Res. 43: D204-D212 (2015).

(2)
RefSeq: an update on mammalian reference sequences. Nucleic Acids Res. 2014 Jan 1;42(1):D756-63.

(3)
Cock PJ et al. Bioinformatics (2009)

(4)
Cokelaer et al, Bioinformatics (2013)
