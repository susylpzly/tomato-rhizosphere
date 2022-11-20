#import libraries
import glob 
import pandas as pd 
import re 
import numpy as np
import sys 

#list of files from directory folder 
#The glob module finds all the pathnames matching a specified pattern
input_path = sys.argv[1]
#output_file = sys.argv[2]


filenames = glob.glob(input_path + "/T*.tsv") 

file_list = []
for file in filenames:
    name = re.search('output/(.+?).tsv', file)
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