import numpy as np
import re

# '/Users/Julia/Downloads/rosalind_cons.txt'
with open('/Users/Julia/Downloads/rosalind_cons-2.txt', 'r') as f:
    text = re.sub(r'Rosalind_\d+', '', f.read())
    # print(text)
    seqs_lst = text.replace('\n', '').split('>')
# print(seqs_lst)

seqs = np.array([list(s) for s in seqs_lst[1:]])
print(seqs[0])
counts = np.zeros((4, seqs.shape[1]), dtype=int)

nuc_list = ['A', 'C', 'G', 'T']
con_seq = ''
for i in range(seqs.shape[1]):
    counts[0,i] += np.sum(seqs[:,i]=='A')
    counts[1,i] += np.sum(seqs[:,i]=='C')
    counts[2,i] += np.sum(seqs[:,i]=='G')
    counts[3,i] += np.sum(seqs[:,i]=='T')
    
    con_seq += nuc_list[np.argmax(counts[:,i])]

with open('consensus_out.txt', 'w') as f:
    print(con_seq, file=f)
    for i in range(4):
        # print(str.join(counts[i]))
        print(f'{nuc_list[i]}: ', end='', file=f)
        print(*counts[i], file=f)