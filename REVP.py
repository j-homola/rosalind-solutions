import dna_functions as dnaf
import fasta_reader as fr

file_path = 'your path here'
keys, vals = fr.read_fasta(file_path, format=list)
seq = vals[0]
# seq = 'TCAATGCATGCGGGTCTATATGCAT'

site_list = []
for k in range(4, 13):
    for i in range(len(seq)-k+1):
        site = seq[i:i+k]
        if site == dnaf.dna_complement(site):
            site_list.append((i+1, k))

with open('output.txt', 'w') as f:
    for s in site_list:
        print(*s, file=f)
