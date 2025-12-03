with open('/Users/Julia/Downloads/rosalind_hamm.txt', 'r') as f:
    seq1, seq2 = [line for line in f]

dist = 0
for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        dist += 1

print(dist)