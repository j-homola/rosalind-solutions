import fasta_reader as fr
import dna_functions as dnaf

keys, vals = fr.read_fasta('/Users/Julia/Downloads/rosalind_splc.txt', format=list)
strand = vals[0]

for seq in vals[1:]:
    strand = strand.replace(seq, '')

r_strand = dnaf.dna_to_rna(strand)
print(dnaf.translate(r_strand))