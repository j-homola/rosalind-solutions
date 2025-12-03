from collections import Counter

with open('/Users/Julia/Downloads/rosalind_deg-3.txt', 'r') as f:
    edges = f.read().split()[2:]
# print(edges[:5])s
edges = [int(e) for e in edges]
counts = Counter(edges)
# verts = sorted(int(k) for k in counts.keys())
# for i in sorted(counts.keys())[:10]:
#       print(i, ":", counts[i])
    
with open('output.txt', 'w') as f:
    print(*[counts[x] for x in sorted(counts.keys())], file=f)