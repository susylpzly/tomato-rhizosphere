## CODE AND SCRIPT LINES USEFUL FOR THINGS 
#To access uva server
ssh -X 14108550@omics-h0.science.uva.nl 

#TO LOOK AT CURRENT JOBS
squeue -u 14108550

#TO LOOK AT THE STATUS OF ALL THE NODES 
sinfo -o "%n %e %m %a %c %C" 

#TO ENTER A COMPUTATION NODE 
srun -w omics-cn002 --pty bash

#TO COPY FILES OR DIRECTORIES FROM REMOTE SERVER TO LOCAL 
scp 14108550@omics-h0.science.uva.nl:/zfs/omics/projects/phb/bora/IMP3/Pfam_output . 

#TO LOOK AT DIRECTORY CONTENTS 
ls -lh 
ls -ltrh 

#TO DRY RUN IMP3 
/zfs/omics/projects/metatools/TOOLS/IMP3/runIMP3 -d ../configs/T_712_2.assembly.config.yaml

#TO REAL RUN IMP3 
/zfs/omics/projects/metatools/TOOLS/IMP3/runIMP3 -c -r -n T_712_2 -b omics-cn003 ../configs/T_712_2.assembly.config.yaml

#TO ACTIVATE ANTISMASH
conda activate /zfs/omics/projects/metatools/TOOLS/miniconda3/envs/antismash6/ 
    #TO GET HELP FOR ANTISMASH
    > antismash -h (to learn how to run it with flags and everything)
    antismash mg.assembly.merged.length_filtered.fa --genefinding-gff3 annotation.assembly_filt.gff -c 8 --output-dir t
    #TO CLOSE ANTISMASH 
    antismash mg.assembly.merged.fa --genefinding-gff3 annotation.filt.gff -c 8 --allow-long-headers --minlength 10000 --asf --clusterhmmer --cb-knownclusters --rre --cb-subcluster
    > conda deactivate once done using it 

#code ran for antismash - multiple parameters - took 50 mins 
antismash mg.assembly.merged.length_filtered.fa --genefinding-gff3 annotation.assembly_filt.gff -c 8 --output-dir antismash_output --smcog-trees --clusterhmmer --cb-subcluster --cb-knownclusters

#TO KILL A RUN
do scancel +number of run to cancel a run

#to filter the assembly output based on length of contig 
reformat.sh in=mg.assembly.merged.fa out=mg.assembly.merged.length_filtered.fa minlength=10000

#to use python script to filter gff based on annotation file contigs 
python3 gff_filtering.py T_712_2/annotation.filt.gff T_712_2/mg.assembly.merged.length_filtered.fa T_712_2/annotation.assembly_filt.gff


conda activate /zfs/omics/projects/metatools/TOOLS/IMP3/conda/8fab667c26067cc13be382368594bb18

featureCounts environment 

featureCounts -p -O -t CDS -g db_xref -o antismash.Pfam.counts.tsv -s 0 -a mg.db_xref.counts.gff -T 1 /zfs/omics/projects/phb/bora/IMP3/T_712_11/Assembly/mg.reads.sorted.bam