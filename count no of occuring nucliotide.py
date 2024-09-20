def countNucFrequency(seq):
    A_count = seq.count('A')
    C_count = seq.count('C')
    G_count = seq.count('G')
    T_count = seq.count('T')
    return A_count, C_count, G_count, T_count

# DNA sequence
DNAString = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

# Get nucleotide frequencies
A, C, G, T = countNucFrequency(DNAString)

# Print nucleotide frequencies without labels
print(A, C, G, T)
