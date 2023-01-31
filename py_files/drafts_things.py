# Script to filter the gff annotation file from the filtered .fa assembly file 
# Get the contigs of the annotation file that exist in the assembly

import sys

def filtering(ann_file, ass_file):
    #Open the files
    annotations = open(ann_file, "r")
    assemblies = open(ass_file, "r")

    newannotations = open('annotation.assembly_filt.gff','w')
    #Results in a list of lines, in column organization 
    out_file = [] 

    contig_IDs = []
    #Make a list of the contig names in the assembly file
    for line in assemblies:
        if line.startswith('>'):
            contig_ID = line 
            #remove the '>' from the contigID 
            contig_ID = contig_ID.replace('>','')
            contig_IDs.append(contig_ID) 

    
    for line in annotations:
        #Separate the columns from the .gff file and take first element as value variable
        columns = line.strip().split('\t')
        value = columns[0]
        if value in contig_IDs:
            #add the line to the file 
            out_file.append(line)
        else:
            pass 
     
    for element in out_file:
        newannotations.write(element + '\n')


    #Remeber to close files after done
    annotations.close()
    assemblies.close() 
    newannotations.close()

    #Return the filtered gff file 
    return 'annotation.assembly_filt.gff'

def main():
    ann_file = sys.argv[1]
    ass_file = sys.argv[2]
    'annotation.assembly_filt.gff' = filtering(ann_file,ass_file)


if __name__ == '__main__':
    main()