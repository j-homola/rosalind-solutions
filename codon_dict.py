import re

def get_codons():
    with open('codon_table.txt', 'r') as f:
        codons = re.split(r"\n|\s{2,}", f.read())

    codon_dict = {}
    for c in codons:
        a, b = c.split()
        codon_dict[a] = b

    return codon_dict