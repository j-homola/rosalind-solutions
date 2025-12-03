from collections import Counter

file_path = 'your path here'
with open(file_path, 'r') as f:
    edges = f.read().split()[2:]

edges = [int(e) for e in edges]
counts = Counter(edges)
    
with open('output.txt', 'w') as f:
    print(*[counts[x] for x in sorted(counts.keys())], file=f)
