from collections import Counter

with open('/Users/Julia/Downloads/rosalind_ddeg.txt', 'r') as f:
    n, v, edges = f.read().split(maxsplit=2)

n = int(n)
nodes = edges.split()
nodes = [int(x) for x in nodes]

verts = edges.split('\n')
verts = [[int(y) for y in x.split()] for x in verts][:-1]

counts = Counter(nodes)
d2_counts = dict.fromkeys(range(1, n+1), 0)

for v in verts:
    print(v[0], v[1])
    d2_counts[v[0]] += counts[v[1]]
    d2_counts[v[1]] += counts[v[0]]

with open('output.txt', 'w') as f:
    print(*[d2_counts[x] for x in sorted(d2_counts.keys())], file=f)