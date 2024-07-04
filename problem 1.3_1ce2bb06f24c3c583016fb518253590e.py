# python
# Copy code
def probability_kmers_destroyed(e, k, d):
    p_error_free = (1 - e) ** k
    p_destroyed = 1 - p_error_free
    p_all_destroyed = p_destroyed ** d
    return p_all_destroyed

e1 = 0.01
e2 = 0.025
k = 21
d = 100

p_all_destroyed_e1 = probability_kmers_destroyed(e1, k, d)
p_all_destroyed_e2 = probability_kmers_destroyed(e2, k, d)

p_all_destroyed_e1, p_all_destroyed_e2