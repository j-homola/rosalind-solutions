import fasta_reader as fr

file_path = 'your path here'
seq_dict = fr.read_fasta(file_path)

values = list(seq_dict.values())

def find_matches(vals, k):
    for i in range(len(vals[0])-k):
        motif = vals[0][i:i+k]
        match = True
        for v in vals[1:]:
            if motif not in v:
                match = False
                break   
        if match:
            return motif
    return None

for k in range(len(values[0]), 1, -1):
    motif = find_matches(values, k)
    if motif is not None:
        print(motif)
        break
