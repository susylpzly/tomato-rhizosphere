# Script to filter the gff annotation file from the filtered .fa assembly file 
# Get the contigs of the annotation file that exist in the assembly

import sys

ann_file = sys.argv[1]
ass_file = sys.argv[2]
#out_file = sys.argv[3]
    
#Open the files
annotations = open(ann_file, "r")
assemblies = open(ass_file, "r")

new_ann_file = open(sys.argv[3],'w')
#Results in a list of lines, in column organization 
new_annotations = [] 

contig_IDs = []
#Make a list of the contig names in the assembly file
for line in assemblies:
    if line.startswith('>'):
        contig_ID = line 
        #remove the '>' and the '\n' from the contigID 
        contig_ID = contig_ID.replace('>','')
        contig_ID = contig_ID.replace('\n','')
        contig_IDs.append(contig_ID) 

    
for line in annotations:
    #Separate the columns from the .gff file and take first element as value variable
    columns = line.strip().split('\t')
    value = columns[0]
    if value in contig_IDs:
        #add the line to the file 
        new_annotations.append(line)
    else:
        pass 

#Write all the found contigs into the output file 
for element in new_annotations:
    new_ann_file.write(element + '\n')


#Remeber to close files after done
annotations.close()
assemblies.close() 
new_ann_file.close()