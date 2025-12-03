file_path = 'your path here'
with open(file_path, 'r') as f:
    seqs = f.read().split(">")

max_id = ""
max_gc = 0

for i in range(1,len(seqs)):
    id, s = seqs[i].split("\n", 1)
    s = s.replace("\n", "")
    gc = s.count("G") + s.count("C")
    gc_pct = gc / len(s.strip()) * 100
    
    if gc_pct > max_gc:
        max_id = id
        max_gc = gc_pct

print(max_id)
print(max_gc)
