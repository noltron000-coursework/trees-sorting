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
	items[:] = merge(items1, items2)

def merge_sort(items):
	'''
		Sort given items by splitting list into two
		approximately equal halves, sorting each recursively,
		and merging results into a list in sorted order.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	# Check base case: the list is so small
	# that it is already sorted.
	if len(items) <= 1:
		return items

	# Split items list into approximately equal halves.
	items1 = items[:len(items)//2]
	items2 = items[len(items)//2:]
	# Sort each half by recursively calling merge sort.
	items1 = merge_sort(items1)
	items2 = merge_sort(items2)

	# Merge sorted halves into one list in sorted order.
	items[:] = merge(items1, items2)

def partition(items, low, high):
	'''
		Return index `pivot` after in-place partitioning given
		items in range `[low...high]` by choosing a pivot
		(TODO: document your method here) from that range,
		moving pivot into index `pivot`, items less than pivot
		into range `[low...pivot-1]`, and items greater than
		pivot into range `[pivot+1...high]`.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	# Choose a pivot by selecting first available index.
	# Pivot starts equal to low, but increases with each swap.
	pivot = low
	# ==FIXME==
	# For now, we also take the value at pivot: the first index.
	# pivot_value = items[low]

	# ==FIXME==
	# This is a temporary array to help solidify concepts.
	low_range = []
	high_range = []

	# Loop through all other items in range (sans low).
	# print([pivot] + list(range(low+1, high)))
	for selected in range(low + 1, high):
		# Move items less than pivot into front of range.
		# [low...pivot-1]
		if items[selected] <= items[low]:
			low_range.append(items[selected])
			pivot += 1

		# Move items greater than pivot into back of range.
		# [pivot+1...high]
		elif items[selected] > items[low]:
			high_range.append(items[selected])

	# ==FIXME==
	# This solution helps me understand the function.
	print(items[low:high])
	items[low:high] = low_range + [items[low]] + high_range
	print(items[low:high])
	# Move pivot item into final position [pivot],
	# and then return the index of pivot.
	return pivot

def quick_sort(items, low=None, high=None):
	'''
		Sort given items in place by partitioning items in
		range `[low...high]` around a pivot item and
		recursively sorting each remaining sublist range.
		TODO: Best case running time: ??? Why and under what conditions?
		TODO: Worst case running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	# Check if high and low range bounds
	# have default values (not given).
	if low is None:
		low = 0
	if high is None:
		high = len(items)

	# Base Case:
	# The list is so small that it is already sorted.
	if high - low < 0:
		raise
	elif high - low < 2:
		return

	# Partition items in-place around a pivot,
	# and then get the index of that pivot.
	pivot = partition(items, low, high)

	# Recursively call quick_sort to sort each sublist range.
	quick_sort(items, low, pivot)
	quick_sort(items, pivot + 1, high)
