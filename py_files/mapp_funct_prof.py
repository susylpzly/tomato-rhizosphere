#Script to build the Functional Profiles from directory of tsv files of database annotation
#to include all the functions together into a matrix with the mapped count reads for each function observed 
#import libraries
import glob 
import pandas as pd 
import re 
import numpy as np
import sys 




#take the input argument - directory path to where all the files to read are 
input_path = sys.argv[1]

#The glob module finds all the pathnames matching a specified pattern
#list of files from directory folder 
filenames = glob.glob(input_path + "/T*.tsv") 

file_list = []
#for each file(by calling the name) in the list of file names
for file in filenames:
    #get the portion of the file name which is unique - sample name
    name = re.search('output/(.+?).tsv', file)
    #
    if name:
        column_name = name.group(1)
    sample_df = pd.read_table(file, sep='\t', skiprows = 1, index_col='Geneid', usecols=['Geneid','Assembly/mg.reads.sorted.bam'], header = 0)
    sample_df.rename(columns={'Assembly/mg.reads.sorted.bam': column_name}, inplace= True)
    file_list.append(sample_df)

#Concatenate all DataFrames
#samples with no reads mapped to certain KOs are filled with NaNs 
big_df   = pd.concat(file_list, axis = 1 , join = 'outer')


#output a csv file
big_df.to_csv("dbCAN_profile.csv")