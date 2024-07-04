# python
# Copy code
def assign_reads_to_genomes(reads, discriminative_kmers, k):
    genome_assignments = []

    for read in reads:
        assigned_genome = None
        for genome_id, kmers in discriminative_kmers.items():
            for i in range(len(read) - k + 1):
                kmer = read[i:i + k]
                if kmer in kmers:
                    assigned_genome = genome_id
                    break
            if assigned_genome is not None:
                break
        genome_assignments.append(assigned_genome)

    return genome_assignments