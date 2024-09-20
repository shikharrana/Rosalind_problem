DNA_ReverseComplement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


def reverse_complement(seq):
    """Swapping adenine with thymine and guanine with cytosine. Reversing newly generated string"""
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]


print(reverse_complement("AAAACCCGGT"))

#SECOND PROGRAM 
def reverse_complement(seq):
    complement = ""
    for nuc in seq:
        if nuc == 'A':
            complement += 'T'
        elif nuc == 'T':
            complement += 'A'
        elif nuc == 'G':
            complement += 'C'
        elif nuc == 'C':
            complement += 'G'
    return complement[::-1]

# Example usage
print(reverse_complement("AAAACCCGGT"))
#...
def reverse_complement(dna_sequence):
    # Define a translation table for base complementing
    complement = str.maketrans('ATCG', 'TAGC')
    
    # Get the complementary sequence
    complement_sequence = dna_sequence.translate(complement)
    
    # Reverse the complementary sequence
    reverse_complement_sequence = complement_sequence[::-1]
    
    return reverse_complement_sequence

# Example DNA sequence
dna_sequence = ("TATTATAATACAATAGTATCTCGCGGATATCCACGGGGCTTCTAGCACAACCGATAATATCTTCCCACGAGCAGAATCTTCACTACATCTCTAAATTATTGCGTCGGTGGGGACCTATACTTTACCTGCTGTAGTGGGGACAACGTGGGTCGGTCTTAACTCCGAGGAACACTGTTCGGACGCGGTAGTAATACCGCTAGACCATATAATCCCAACATACGCGCCTGCCAGGCCCTACCCGTGATAGCGGTTCCGAAACGATATAGTTAATCGTTGCGCCAAGCAGGTTCATACCCGACGGGACGGGGTTTTAGGCTAGTGATTACTGATGCTTTCTGCAACTACCTAAAGGATGTGCTACTTGATATACTAAGCGCACATGTATAACCCTCGTCAGATAAAACTGTCGTACGGCAAGTTAGACGAGACTAAGGGCACACGTCGCAATCCATAATGCATTAAGTTGGCTAGCGGCAGCCCTCTTTGTCCAACAACTTTCCCCGTCGAATGTAGGCCTTATCGTCATACCGGAACCCTCGCTAGTAAACGCCTAAAGGCTGGTCCAGGCCTGAGCCCGGCGGTTCTCGGTTTACTCAGCACGATACAGCGGACGTTTGATACTGCTCTATTTAGTATAAGACTACCTCATCCGGGCAGCTCAGTAACTATAGCAACCAGGTGGAACTCATTCCGAGCCCGTTGGTAGTATGAATGGCGGTCAGCGCGTCGTAGCACTATGGTACGGACCGTTTGACACCGGCTGTCTCTCTGGCCCACCCCAACGGTCGTCGATCGGGCTGTTCGTCCACCGTGTTAGTATCAAATGATTTTGACGGGTGTCATGTTATCTCTTTTAT")
reverse_complement_sequence = reverse_complement(dna_sequence)
print(reverse_complement_sequence)