#Script to parse all regions Genbank files from antismash output to a single gff file 

#import libraries 
import glob 
import sys 
from Bio import SeqIO


#take the input argument - directory path to where all the files to read are 
input_path = sys.argv[1]

#The glob module finds all the pathnames matching a specified pattern
#list of files from directory folder 
filenames = glob.glob(input_path + "/test_contig_*.gbk") 


#function to write the genbank file region features into lines for each file(contig)
def make_lines(file_path):
    genome_record = SeqIO.read(file_path, 'genbank')
    
    lines = []
    line = ''
    for i in range(len(genome_record.features)):
        #check if the type of region/feature is a coding sequence/annotated region with the 'phase' qualifier/key, to also include along the line
        if genome_record.features[i].qualifiers.__contains__('phase'):
            #check if annotation is from a 'tool' a 'aStool' or a 'source' to include in the second column 
            if genome_record.features[i].qualifiers.__contains__('tool'):
                string = str(genome_record.description) + '\t' + str(genome_record.features[i].qualifiers['tool'][0]) + ' ' + str(genome_record.features[i].type) + '\t' + str(genome_record.features[i].location.start) + '\t' + str(genome_record.features[i].location.end) + '\t' + '.' + '\t' + str(genome_record.features[i].location)[-2] + '\t' + str(genome_record.features[i].qualifiers['phase'][0]) + '\t'
            else:
                if genome_record.features[i].qualifiers.__contains__('aStool'):
                    string = str(genome_record.description) + '\t' + str(genome_record.features[i].qualifiers['aStool'][0]) + ' ' + str(genome_record.features[i].type) + '\t' + str(genome_record.features[i].location.start) + '\t' + str(genome_record.features[i].location.end) + '\t' + '.' + '\t' + str(genome_record.features[i].location)[-2] + '\t' + str(genome_record.features[i].qualifiers['phase'][0]) + '\t'
                else:
                    string = str(genome_record.description) + '\t' + str(genome_record.features[i].qualifiers['source'][0]) + ' ' + str(genome_record.features[i].type) + '\t' + str(genome_record.features[i].location.start) + '\t' + str(genome_record.features[i].location.end) + '\t' + '.' + '\t' + str(genome_record.features[i].location)[-2] + '\t' + str(genome_record.features[i].qualifiers['phase'][0]) + '\t'
        else:
            if genome_record.features[i].qualifiers.__contains__('tool'):
                string = str(genome_record.description) + '\t' + str(genome_record.features[i].qualifiers['tool'][0]) + ' ' + str(genome_record.features[i].type) + '\t' + str(genome_record.features[i].location.start) + '\t' + str(genome_record.features[i].location.end) + '\t' + '.' + '\t' + str(genome_record.features[i].location)[-2] + '\t' 
            else:
                if genome_record.features[i].qualifiers.__contains__('aStool'):
                    string = str(genome_record.description) + '\t' + str(genome_record.features[i].qualifiers['aStool'][0]) + ' ' + str(genome_record.features[i].type) + '\t' + str(genome_record.features[i].location.start) + '\t' + str(genome_record.features[i].location.end) + '\t' + '.' + '\t' + str(genome_record.features[i].location)[-2] + '\t'
                else:
                    string = str(genome_record.description) + '\t' + str(genome_record.features[i].qualifiers['source'][0]) + ' ' + str(genome_record.features[i].type) + '\t' + str(genome_record.features[i].location.start) + '\t' + str(genome_record.features[i].location.end) + '\t' + '.' + '\t' + str(genome_record.features[i].location)[-2] + '\t'
        
        attributess = ''
        for key in genome_record.features[i].qualifiers:
        #print(i, qualif_dict[i])
            if key ==  'ID' or key == 'gene' or key == 'translation' or key == 'partial' or key == 'domain_id':
                pass
            else:
                if len(genome_record.features[i].qualifiers[key]) > 1:
                    temp = str(key) + '=' + str(genome_record.features[i].qualifiers[key]) + ';' 
                    attributess = attributess + str(temp)
                else:
                #print(len(genome_record.features[i].qualifiers[key]))
                    temp = str(key) + '=' + str(genome_record.features[i].qualifiers[key][0]) + ';' 
                    attributess = attributess + str(temp)
        #attributess 
        line = line + string + attributess
        lines.append(str(line))
        line = ''
    #return list of all the lines 
    return lines 


#loop over all the gbk files in the list and apply the above function to all
file_list = []
#for each file(by calling the name) in the list of file names
for file in filenames:
    #
    tmp_file = make_lines(file)
    file_list = file_list + tmp_file


#write gff outfile with all the types entrees for antismash annotation from gbk file 
with open(r'./mg.all.gff', 'w') as out:
    #for line in lines: 
    #    out.write('\n' % line)
    out.write('\n'.join(file_list))

#write gff outfile for CDS regions which have actual annotated locus tags with identified gene_functions
with open(r'./mg.CDS.counts.gff', 'w') as CDS_out:
    for line in file_list:
        if line.__contains__('gene_functions'):
            CDS_out.write(line + '\n')

#write gff outfile for found regions from Pfam database 
with open(r'./mg.Pfam.counts.gff', 'w') as Pfam_out:
    for line in file_list:
        if line.__contains__('PFAM_domain'):
            Pfam_out.write(line + '\n')

with open(r'./mg.aSDomain.counts.gff', 'w') as aSDomain_out:
    for line in file_list:
        if line.__contains__(' aSDomain	'):
            aSDomain_out.write(line + '\n')

out.close()
CDS_out.close()
Pfam_out.close() 
aSDomain_out.close()