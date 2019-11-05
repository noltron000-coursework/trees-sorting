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
	# ==TODO==
	# Find range of given numbers (min/max values)

	# ==TODO==
	# Create list of buckets to store
	# numbers in subranges of input range.

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
