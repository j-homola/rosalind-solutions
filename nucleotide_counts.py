with open('/Users/Julia/Downloads/rosalind_dna-3.txt', 'r') as f:
    seq = f.read()

a_count = seq.count("A")
t_count = seq.count("T")
c_count = seq.count("C")
g_count = seq.count("G")
# for char in seq:
#     if char.equals('A'):
#         a_count += 1
#     if char.equals('T'):
#         t_count += 1
#     if char.equals('C'):
#         c_count += 1
#     if char.equals('G'):
#         g_count += 1

print(f"{a_count} {c_count} {g_count} {t_count}")