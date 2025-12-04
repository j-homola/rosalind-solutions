import re

file_path = 'your path here'

with open(file_path, 'r') as f:
    seq, patt = f.read().strip().split('\n')

matches = re.finditer(rf"(?=({patt}))", seq)

print(*[m.start() + 1 for m in matches])
