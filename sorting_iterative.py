def is_sorted(items):
	'''
		Return a boolean indicating whether
		given items are in sorted order.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	# Check that all adjacent items are in order.
	for index, current_item in enumerate(items):
		# The first item gets a free pass.
		if index != 0:
			previous_item = items[index - 1]
			# Return early if items is not in order.
			if previous_item > current_item:
				return False
	# If the loop finishes, then its in order.
	else:
		return True

def bubble_sort(items):
	'''
		Sort given items by swapping adjacent items
		that are out of order, and repeating until
		all items are in sorted order.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	# Initialize loop variable as `> 0`.
	swaps = 1
	# Repeat until all items are in sorted order.
	while swaps > 0:
		# Reset number of swaps for this iteration.
		swaps = 0
		# Loop through every element.
		for index in range(len(items)):
			# The first item gets a free pass.
			if index != 0:
				current_item = items[index]
				previous_item = items[index - 1]
				# Check if adjacent items are out of order.
				if previous_item > current_item:
					# Swap adjacent items that are out of order.
					items[index] = previous_item
					items[index - 1] = current_item
					# Mark number of swaps.
					swaps += 1
	return items

def selection_sort(items):
	'''
		Sort given items by finding minimum item,
		swapping it with first unsorted item,
		and repeating until all items are in sorted order.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	# ==TODO==
	# Repeat until all items are in sorted order.

	# ==TODO==
	# Find minimum item in unsorted items.

	# ==TODO==
	# Swap it with first unsorted item.

	pass


def insertion_sort(items):
	'''
		Sort given items by taking first unsorted item,
		inserting it in sorted order in front of items,
		and repeating until all items are in order.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	# ==TODO==
	# Repeat until all items are in sorted order.

	# ==TODO==
	# Take first unsorted item.

	# ==TODO==
	# Insert it in sorted order in front of items.

	pass
