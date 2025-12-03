import itertools

with open('/Users/Julia/Downloads/rosalind_perm-2.txt', 'r') as f:
    n = int(f.read())
# n = 3
perms = list(itertools.permutations(range(1, n+1)))

with open('output.txt', 'w') as f:
    print(len(perms), file=f)
    for p in perms:
        print(*p, file=f)