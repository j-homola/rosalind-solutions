with open('/Users/Julia/Downloads/rosalind_fibd.txt', 'r') as f:
    n, m = f.read().split()
# n, m = [6, 3]
n = int(n)
m = int(m)
new_pairs = [1]
for i in range(n-1):
    if i <= m:
        new_pairs.append(sum(new_pairs[:i]))
    else:
        new_pairs.append(sum(new_pairs[i-m+1:i]))
    
# print(new_pairs)
print(sum(new_pairs[n-m+1:]))