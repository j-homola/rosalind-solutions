import fasta_reader as fr

seq_dict = fr.read_fasta("/Users/Julia/Downloads/rosalind_grph-4.txt")
# print(seq_dict)

keys = list(seq_dict.keys())
vals = list(seq_dict.values())

pairs = []
for i in range(len(vals)-1):
    for j in range(i+1, len(vals)):
        if vals[i][-3:] == vals[j][:3]:
            pairs.append([keys[i], keys[j]])
        if vals[j][-3:] == vals[i][:3]:
            pairs.append([keys[j], keys[i]])

with open('output.txt', 'w') as f:
    for p in pairs:
        print(*p, file=f)