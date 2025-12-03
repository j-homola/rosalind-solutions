n = 24    #enter n here

fib = [0, 1]
if n >= 2:
    for i in range(2, n+1):
        fib.append(fib[-1] + fib[-2])

print(fib[-1])
