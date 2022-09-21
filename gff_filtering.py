# Script to filter the gff annotation file from the filtered .fa assembly file 
# Get the contigs of the annotation file that exist in the assembly

import sys

def filtering(ann_file, ass_file):
    #Open the files
    annotations = open(ann_file, "r")
    assemblies = open(ass_file, "r")

    #Results in a list of lines, in column organization 
    out_file = [] 

    #Make a list of the contig names in the assembly file
    for line in assemblies:
        if line.startswith('>'):
            contig_ID = line 

    
    for line in annotations:
        #Separate the columns from the .gff file and take first element as value variable
        columns = line.strip().split('\t')
        value = columns[0]
    



    #Remeber to close files after done
    annotations.close()
    assemblies.close() 

    #Return the filtered gff file 
    return out_file 

def main():
    ann_file = sys.argv[1]
    ass_file = sys.argv[2]
    out_file = filtering(ann_file,ass_file)


if __name__ == '__main__':
    main()