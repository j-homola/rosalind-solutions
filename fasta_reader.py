def read_fasta(path, format=dict):
    """
    Input: file path containing sequences in FASTA format
    
    Output: dictionary mapping names to sequences
    """
    with open(path, 'r') as f:
        text = f.read().split('\n')

        seq_dict = {}
        curr_key = None
        curr_seq = None

        for line in text:
            if len(line)>0:
                if line[0] == '>':
                    if curr_seq is not None:
                        seq_dict[curr_key] = curr_seq
                    curr_key = line[1:]
                    curr_seq = ''

                elif curr_key is not None:
                    curr_seq += line
        # add last seq
        if curr_key is not None:
            seq_dict[curr_key] = curr_seq
    if format == dict:
        return(seq_dict)
    if format == list:
        return(list(seq_dict.keys()), list(seq_dict.values()))