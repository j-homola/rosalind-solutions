with open('/Users/Julia/Downloads/rosalind_fib.txt', 'r') as f:
    n, k = f.read().split()
print(n, k)
counts = []
for i in range(int(n)):
    if i > 0:
        c = counts[i-1]
    else: c = 1
    if i > 1:
        c += counts[i-2] * int(k)
    counts.append(c)

print(counts[-1])