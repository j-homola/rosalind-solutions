file_path = 'your path here'
with open(file_path, 'r') as f:
    n, m, arr_nums = f.read().split('\n', maxsplit=2)

n = int(n)
m = int(m)

arr_nums = arr_nums.split()
arr = [int(x) for x in arr_nums[:n]]
nums = [int(x) for x in arr_nums[n:]]

mid_ind = n//2
mid = arr[mid_ind]
inds = []

for x in nums:
    if int(x) < mid:
        start = 0
        stop = mid_ind
    elif int(x) > mid:
        start = mid_ind+1
        stop = n
    else:
        inds.append(mid_ind)
        continue

    for i in range(start, stop):
        if x == arr[i]:
            inds.append(i+1)
            break
    else:   # only execute if no break
        inds.append(-1)

with open('output.txt', 'w') as f:
    print(*inds, file=f)
