import re

with open('codon_table.txt', 'r') as f:
    codons = re.split(r"\n|\s{2,}", f.read())

codon_dict = {}
for c in codons:
    a, b = c.split()
    codon_dict[a] = b

file_path = 'your path here'
with open(file_path, 'r') as f:
    seq = f.read()
# seq = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
i = 0
out = ''
start = False

while i < len(seq):
    cod = seq[i:i+3]
    prot = codon_dict[cod]
    if prot == "M":
        start = True
    if start:
        if prot != 'Stop':
            out += prot
        else:
            break
        i += 3
    else:
        i += 1

print(out)
