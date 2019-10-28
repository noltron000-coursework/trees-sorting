def merge(items1, items2):
	'''
		Merge given lists of items, each assumed to already be
		in sorted order, and return a new list containing all
		items in sorted order.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	items = []
	# Repeat until one list is empty.
	while items1 and items2:
		# Find minimum item in both lists,
		# and then append it to new list.
		if items1[0] < items2[0]:
			items.append(items1[0])
			del items1[0]
		else:
			items.append(items2[0])
			del items2[0]
	# Append remaining items in non-empty list to new list.
	if items1:
		items = items + items1
	elif items2:
		items = items + items2
	return items

def split_sort_merge(items):
	'''
		Sort given items by splitting list into two
		approximately equal halves, sorting each with an
		iterative sorting algorithm, and merging results
		into a list in sorted order.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	# Split items list into approximately equal halves.
	items1 = items[:len(items)//2]
	items2 = items[len(items)//2:]
	# Sort each half using any other sorting algorithm.
	items1.sort()
	items2.sort()

	# Merge sorted halves into one list in sorted order.
	items = merge(items1, items2)
	return items

def merge_sort(items):
	'''
		Sort given items by splitting list into two
		approximately equal halves, sorting each recursively,
		and merging results into a list in sorted order.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	# ==TODO==
	# Check base case: the list is so small
	# that it is already sorted.

	# ==TODO==
	# Split items list into approximately equal halves.

	# ==TODO==
	# Sort each half by recursively calling merge sort.

	# ==TODO==
	# Merge sorted halves into one list in sorted order.

	pass

def partition(items, low, high):
	'''
		Return index `p` after in-place partitioning given
		items in range `[low...high]` by choosing a pivot
		(TODO: document your method here) from that range,
		moving pivot into index `p`, items less than pivot
		into range `[low...p-1]`, and items greater than
		pivot into range `[p+1...high]`.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	# ==TODO==
	# Choose a pivot any way and document
	# your method in docstring above.

	# ==TODO==
	# Loop through all items in range.
	# [low...high]

	# ==TODO==
	# Move items less than pivot into front of range.
	# [low...p-1]

	# ==TODO==
	# Move items greater than pivot into back of range.
	# [p+1...high]

	# ==TODO==
	# Move pivot item into final.
	# position [p] and return index p

	pass

def quick_sort(items, low=None, high=None):
	'''
		Sort given items in place by partitioning items in
		range `[low...high]` around a pivot item and
		recursively sorting each remaining sublist range.
		TODO: Best case running time: ??? Why and under what conditions?
		TODO: Worst case running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	# ==TODO==
	# Check if high and low range bounds
	# have default values (not given).

	# ==TODO==
	# Check base case: the list is so small
	# that it is already sorted.

	# ==TODO==
	# Partition items in-place around a pivot
	# and get index of pivot.

	# ==TODO==
	# Sort each sublist range by
	# recursively calling quick sort.

	pass
