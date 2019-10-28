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
	# If the loop finishes, then it is in order.
	return True

def bubble_sort(items):
	'''
		Sort given items by swapping adjacent items
		that are out of order, and repeating until
		all items are in sorted order.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	# Initialize loop variables.
	# ==NOTE==
	# These variables are initialized to some weird integers.
	# Swaps gets the while loop going, and loops becomes 0.
	swaps = 1
	loops = -1
	# Repeat until all items are in sorted order.
	while swaps > 0:
		# Reset number of swaps for this iteration.
		swaps = 0
		# Increment the iteration counter by one.
		loops += 1
		# Loop through every element (up to loops).
		for index in range(len(items) - loops):
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
	# Repeat until all items are in sorted order.
	starter_range = range(len(items))
	for starter_index in starter_range:
		# Grab value like enumerate() would.
		starter_value = items[starter_index]

		# Initialize smallest index/value.
		smallest_index = starter_index
		smallest_value = starter_value

		# Find minimum item in unsorted items.
		checker_range = range(starter_index + 1, len(items))
		for checker_index in checker_range:
			# Grab value like enumerate() would
			checker_value = items[checker_index]

			# Initialize comparison here.
			if smallest_value > checker_value:
				smallest_index = checker_index
				smallest_value = checker_value

		# Swap it with starter item; the first unsorted value.
		items[starter_index] = smallest_value
		items[smallest_index] = starter_value
	return items

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
