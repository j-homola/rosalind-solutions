import re

with open('/Users/Julia/Downloads/rosalind_subs-2.txt', 'r') as f:
    seq, patt = f.read().strip().split('\n')
# print(seq, patt)
# seq = str.join(text[:-1])
# patt = text[-1]

matches = re.finditer(rf"(?=({patt}))", seq)
print(*[m.start() + 1 for m in matches])