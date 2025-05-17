#write functions here, don't add input('') statements here!

def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    """Return all starting positions (1-based) of dna_string2 in dna_string1."""
    positions = []
    for i in range(len(dna_string1) - len(dna_string2) + 1):
        if dna_string1[i:i+len(dna_string2)] == dna_string2:
            positions.append(i + 1)  # Convert to 1-based index
    return tuple(positions)  # Returns multiple values as a tuple
