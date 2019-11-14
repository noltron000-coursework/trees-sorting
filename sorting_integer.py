def counting_sort(numbers):
	'''
		Sort given numbers (integers) by counting occurrences
		of each number, then looping over counts and copying
		that many numbers into output list.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	# Find range of given numbers (min/max integer values).
	minimum = min(numbers)
	maximum = max(numbers)

	# Create a range of number slots.
	slots = []
	for number in range(minimum, maximum + 1):
		slots.append([number, 0])

	# Loop over given numbers and
	# increment each number's count.
	for number in numbers:
		index = minimum - number
		slots[index][1] += 1

	# Loop over counts and append
	# that many numbers into output list.
	result = []
	for slot in slots:
		number = slot[0]
		count = slot[1]
		result += [number] * count

	numbers[:] = result

def bucket_sort(numbers, num_buckets=10):
	'''
		Sort given numbers by distributing into buckets
		representing subranges, then sorting each bucket
		and concatenating all buckets in sorted order.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	# Find range of given numbers (min/max integer values).
	minimum = min(numbers)
	maximum = max(numbers)

	# 0 > 0/1 layers
	# 1 > 1 layer
	# 10 > 2 layers
	# 100 > 3 layers
	layer = 1
	# is 10 ** (1 - 1) <= 10 ?
	# 10 > 1.
	# 	at least 1 layer.
	# is 10 ** (2 - 1) <= 10 ?
	# 10 == 10
	# 	at least 2 layers.
	# is 10 ** (3 - 1) <= 10 ?
	# 10 < 100
	# 	not 3 or more layers.
	while num_buckets ** layer <= maximum:
		layer += 1
	assert(num_buckets ** layer > maximum)

	# Create list of buckets to store
	# numbers in subranges of input range.
	buckets = [None] * num_buckets
	for number in numbers:
		if number % num_buckets ** layer

	# ==TODO==
	# Loop over given numbers and
	# place each item in appropriate bucket.

	# ==TODO==
	# Sort each bucket using any sorting algorithm.

	# ==TODO==
	# Loop over buckets and append
	# each bucket's numbers into output list.

	# ==FIXME==
	# Improve this to mutate input
	# instead of creating new output list.


bucket_sort([0])
bucket_sort([1])
bucket_sort([5])
bucket_sort([9])
bucket_sort([10])
bucket_sort([11])
