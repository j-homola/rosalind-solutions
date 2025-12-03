file_path = 'your path here'
with open(file_path, 'r') as f:
    n, arr = f.read().split('\n', 1)

n = int(n)
arr = [int(a) for a in arr.split()]

swaps = 0
for i in range(1, n):
    k = i
    while k > 0 and arr[k] < arr[k-1]:
        arr[k], arr[k-1] = arr[k-1], arr[k]
        swaps += 1
        k -= 1

print(swaps)
