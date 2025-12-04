import math

file_path = 'your path here'
with open(file_path, 'r') as f:
    args = f.read().split()
    k, N = [int(a) for a in args]

prob = 0
for n in range(N, 2**k+1):
    prob += math.factorial(2**k) / (math.factorial(n) * math.factorial(2**k - n)) * (0.25**n) * (0.75**(2**k - n))

print(prob)
