with open('/Users/Julia/Downloads/rosalind_rna.txt', 'r') as f:
    seq = f.read()

rna = seq.replace("T", "U")
print(rna)