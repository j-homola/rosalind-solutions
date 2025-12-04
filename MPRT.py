import urllib.request, re

file_path = 'your path here'
with open(file_path, 'r') as f:
    ids = f.read().split('\n')

seqs = []
for id in ids:
    id = id.split('_')[0]
    url = f"http://www.uniprot.org/uniprot/{id}.fasta"
    with urllib.request.urlopen(url) as response:
        try:
            file_bytes = response.read()
            file_content = file_bytes.decode('utf-8')

            start = file_content.find('\n')
            seqs.append(file_content[start:].replace('\n', ''))

        except urllib.error.URLError as e:
            print(f"Error fetching the URL: {e.reason}")

locs = []
for seq in seqs:
    matches = re.finditer(r'(?=(N[^P][ST][^P]))', seq)
    locs.append([m.start()+1 for m in matches])

with open('output.txt', 'w') as f:
    for i in range(len(locs)):
        if len(locs[i]) > 0:
            print(ids[i], file=f)
            print(*locs[i], file=f)
