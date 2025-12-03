file_path = 'your path here'
with open(file_path, 'r') as f:
    seq = f.read()

a_count = seq.count("A")
t_count = seq.count("T")
c_count = seq.count("C")
g_count = seq.count("G")

print(f"{a_count} {c_count} {g_count} {t_count}")
