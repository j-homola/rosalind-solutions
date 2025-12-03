with open('/Users/Julia/Downloads/rosalind_iprb-2.txt', 'r') as f:
    k, m, n = f.read().split()
k = int(k)
m = int(m)
n = int(n)
# k, m, n = [2, 2, 2]
# One dom parent: 100%
p1 = k / (k+m+n) * (k-1+m+n) / (k+m+n-1) + (m+n) / (k+m+n) * k / (k+m+n-1)

# Both hetero: 75%
p2 = m / (k+m+n) * (m-1) / (k+m+n-1) * 0.75

# Het x recessive: 50%
p3 = (m / (k+m+n) * n / (k+m+n-1) + n / (k+m+n) * m / (k+m+n-1)) * 0.5

# Both recessive: 0% (ignore)
# print(p1, p2, p3)
print(p1 + p2 + p3)