with open('/Users/Julia/Downloads/rosalind_revc.txt', 'r') as f:
    seq = f.read()

comp = ""
for n in seq[::-1]:
    if n == "A":
        comp += "T"
    elif n == "T":
        comp += "A"
    elif n == "C":
        comp += "G"
    elif n == "G":
        comp += "C"

print(comp)