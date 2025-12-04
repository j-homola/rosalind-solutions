import itertools

file_path = 'your path here'

with open(file_path, 'r') as f:
    letters, length = f.read().split('\n')[:2]

letters = letters.split()
length = int(length)

perms = [x for x in itertools.product(letters, repeat=length)]

with open('output.txt', 'w') as f:
    for p in sorted(perms):
        print(*p, sep='', file=f)
