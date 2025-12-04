import codon_dict as cd
from collections import Counter

file_path = 'your path here'
with open(file_path, 'r') as f:
    seq = f.read().replace('\n', '')

codons = cd.get_codons()
counts = Counter(codons.values())

combos = 1
for aa in seq:
    combos = combos * counts[aa] % 1000000

print(combos*counts['Stop'] % 1000000)
