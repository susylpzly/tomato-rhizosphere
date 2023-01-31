#filter assembly file to only include contigs 10,000 bp or longer
reformat.sh in=mg.assembly.merged.fa out=mg.assembly.merged.length_filtered.fa minlength=10000
#filter the annotation file based on the assembly filtered file to only include the above contigs 
#arg1: annotation file to be filtered
#arg2: assembly file filtered - to be used as reference
#arg3: name of filtered annotation file to be output 
python3 gff_filtering.py annotation.filt.gff mg.assembly.merged.length_filtered.fa annotation.assembly_filt.gff


#activate the antiSMASH environment
conda activate /zfs/omics/projects/metatools/TOOLS/miniconda3/envs/antismash6/
#antiSMASH program run with inputs and flags 
antismash mg.assembly.merged.length_filtered.fa --genefinding-gff3 annotation.assembly_filt.gff -c 8 --allow-long-headers --asf --clusterhmmer --cb-knownclusters --rre --cb-subcluster