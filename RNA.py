file_path = 'your path here
with open(file_path, 'r') as f:
    seq = f.read()

rna = seq.replace("T", "U")
print(rna)
