import dna_functions as dnaf
import fasta_reader as fr
import re

file_path = 'your path here'
seq_dict = fr.read_fasta(file_path)
seq = list(seq_dict.values())[0]

rna_seq = dnaf.dna_to_rna(seq)
rna_rev = dnaf.dna_to_rna(dnaf.dna_complement(seq))

def translate_all(r_seq):
    matches = re.finditer(r"AUG", r_seq)
    prot_list = []
    for m in matches:
        start = m.start()
        prot = dnaf.translate(r_seq[start:])
        if len(prot) > 0:
            prot_list.append(prot)
    return prot_list

all_seqs = set(translate_all(rna_seq) + translate_all(rna_rev))

with open('output.txt', 'w') as f:
    print(*all_seqs, sep='\n', file=f)
