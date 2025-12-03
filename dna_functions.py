import codon_dict as cd

def dna_complement(seq):
    """
    returns reverse complement of a dna sequence
    """
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
    return comp

def dna_to_rna(seq):
    """
    converts dna sequence to rna (no reverse)
    """
    return seq.replace("T", "U")

def translate(seq):
    """
    returns the protein translation of an mRNA sequence
    """
    protein = ''
    codon_dict = cd.get_codons()

    for i in range(len(seq)-2)[::3]:
        cod = seq[i:i+3]
        prot = codon_dict[cod]
        if prot == 'Stop':
            return protein
        else:
            protein += prot
    # no stop codon -> return empty string
    return ''