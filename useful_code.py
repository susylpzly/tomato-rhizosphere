## CODE AND SCRIPT LINES USEFUL FOR THINGS 

#TO LOOK AT CURRENT JOBS
squeue -u 14108550

#TO LOOK AT THE STATUS OF ALL THE NODES 
sinfo -o "%n %e %m %a %c %C" 

#TO ENTER A COMPUTATION NODE 
srun -w omics-cn002 --pty bash

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
    #TO CLOSE ANTISMASH 
    > conda deactivate once done using it 

#TO KILL A RUN
do scancel +number of run to cancel a run

