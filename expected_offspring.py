with open('/Users/Julia/Downloads/rosalind_iev.txt', 'r') as f:
    lst = f.read().split()

pop = [int(l) for l in lst]

dom_num = sum(pop[:3]) + 0.75*pop[3] + 0.5*pop[4]

print(dom_num * 2)