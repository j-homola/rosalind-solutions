file_path = 'your path here'

with open(file_path, 'r') as f:
    seq = f.read()
# seq = 'SKADYEK'
mass_dict = {}

with open('iso_mass_table.txt', 'r') as f:
    text = f.read().split('\n')
    for line in text:
        l_split = line.split()
        mass_dict[l_split[0]] = float(l_split[-1])

mass = 0
for char in seq.strip():
    mass += mass_dict[char]

print(mass)
