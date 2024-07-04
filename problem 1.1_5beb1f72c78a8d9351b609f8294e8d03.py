# python
# Copy code
from collections import defaultdict

def get_kmers(sequence, k):
    """Returns all k-mers of a given sequence."""
    return [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

def compute_discriminative_kmers(genomes, k):
    """Computes discriminative k-mers for each genome."""
    kmer_dict = defaultdict(set)
    genome_kmers = defaultdict(list)
    
    for genome_id, sequence in genomes.items():
        kmers = get_kmers(sequence, k)
        genome_kmers[genome_id] = kmers
        for kmer in kmers:
            kmer_dict[kmer].add(genome_id)
    
    discriminative_kmers = {genome_id: set() for genome_id in genomes}
    
    for kmer, genome_ids in kmer_dict.items():
        if len(genome_ids) == 1:  # K-mer is unique to one genome
            genome_id = list(genome_ids)[0]
            discriminative_kmers[genome_id].add(kmer)
    
    return discriminative_kmers

# Example usage
genomes = {
    'genome1': 'ATCGATCGA',
    'genome2': 'GATCGATCG',
    'genome3': 'TCGATCGAA'
}

k = 3
discriminative_kmers = compute_discriminative_kmers(genomes, k)
print(discriminative_kmers)