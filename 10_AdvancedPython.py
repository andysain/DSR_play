"""Write a function count_pairs(N, m) which returns the number of pairs of numbers in the sequence 0...N-1 whose sum is divisible by m.
For example, if N = 3 and m = 2, the pairs are
[(0, 1), (0, 2), (1, 2)]
The sum of each pair respectively is [1, 2, 3], and there is a single pair whose sum is divisible by 2, so the result is 1.
What is the result for (N,m)=(10,2)?
What is the result for (N,m)=(1000,5)?"""

import itertools

def count_pairs(N,m):
 	z = itertools.combinations(range(N),2)
	pair_sum = map(sum,z)
	return len([x for x in pair_sum if x % m == 0])

print count_pairs(10,2)

def count_pairs2(N,m):
 	z = itertools.combinations(range(N),2)
	div_pairs = [(a,b) for a, b in z if (a + b) % m == 0]
	return len(div_pairs)

print count_pairs2(10,2)
