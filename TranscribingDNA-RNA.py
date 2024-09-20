def transcribe_dna_to_rna(dna_sequence):
    return dna_sequence.upper().replace('T', 'U')

# Example usage
dna_sequence = "ACTATGAGTTGATAATAGTCTAAGTGGTCGGACGTCGGAAAAAAGGCCTCACTTTCGTGATAAACTGAGCTTTCCTTAGGCTACTATGAGGATCCATTTAGTTGTAGGAGCTGAGCAAGAAGCATACCAGTGGCTTTACTCTAACTGTTCGGAAGTTACCTAAAAATCGTATGTTTCCTGATCAGTAGGGAAACCGTAACTTTCAATATAAGATCGCGAGGCTGTGTGACATTGCATTGCGGTGACTTAATCCAACATACCCTAGGACCCCGCGGCAAATGACGGTAGGCCCCTCACAGAAGATCAGCATAGGTCTGATGAATATGCTACCGCCTCATCAATTAGAACAAACTTCGGGTTCCTATACGAACGCACTAGAAATGGGTGGGGAGATGAGGAAAGGGGAGTCTCGTGGCGGTATCCCAATATTACCTAATAGGCATATTCGTACAGGAAGAGTAGGAACTTTCTCTGGCCACGGCTAGGAAACCCTGATGGTTGCCGTGAGAAACTAGACCACGAGCCATTTACTTCCCTTCAGTCAAGGAAGCAGACTGTAAGAAGCTACATGTTTGAATGACTCCACTACTCTCTATTGCCGACATGCCATACACATAAGGTGTGACATTCCCAGGCGGGTCACGTCCGTATATTTCTTAACCGACAACCAGTTGGCTCCTCAACGAACGTTTGGGCTCGATCTCCCCCATAACTACCCTTGGTACCGGCACTCGCTCACTTCATTAGCGTGCTCAACGAGGATGCTCCAGCTTCTGGACGAGACCCACAACTCATTCGCGTTCTAGCCGTAAAAGGCAGACTGACCGTGCCGCAATGTCGACTCCAAGTTAGTTACCTTGCTGACTTGGAGGACGGACGTGGGCTAGATTTCCAGGCCACGATTATAGCCCAATAAGCTATTGCGTTAAGCTTGGT"
rna_sequence = transcribe_dna_to_rna(dna_sequence)
print(rna_sequence)