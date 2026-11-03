class BinaryMinHeap(object):
	'''
	BinaryMinHeap: a partially ordered collection with
	efficient methods to insert new items in partial order
	and to access and remove its minimum item.
	Items are stored in a dynamic array that implicitly
	represents a complete binary tree with root node at
	index 0 and last leaf node at index n-1.
	'''

	def __init__(self, items=None):
		'''
		Initialize this heap and insert the given items, if any.
		'''
		# Initialize an empty list to store the items.
		self.items = []
		if items:
			for item in items:
				self.insert(item)

	def __repr__(self):
		'''
		Return a string representation of this heap.
		'''
		return f'BinaryMinHeap({self.items})'

	def is_empty(self):
		'''
		Return True if this heap is empty, or False otherwise.
		'''
		return self.size() == 0

	def size(self):
		'''
		Return the number of items in this heap.
		'''
		return len(self.items)

	def insert(self, item):
		'''
		Insert the given item into this heap.
		==TODO==
		Best case running time:
		??? under what conditions?
		==TODO==
		Worst case running time:
		??? under what conditions?
		'''
		# Insert the item at the end and bubble up to the root.
		self.items.append(item)
		if self.size() > 1:
			self._bubble_up(self._last_index())

	def get_min(self):
		'''
		Return the minimum item at the root of this heap.
		Best and worst case running time: O(1)
		because min item is the root.
		'''
		if self.size() == 0:
			raise ValueError(
				'Heap is empty and has no minimum item'
			)
		assert self.size() > 0
		return self.items[0]

	def delete_min(self):
		'''
		Remove and return the minimum
		item at the root of this heap.
		==TODO==
		Best case running time:
		??? under what conditions?
		==TODO==
		Worst case running time:
		??? under what conditions?
		'''
		if self.size() == 0:
			raise ValueError(
				'Heap is empty and has no minimum item'
			)
		elif self.size() == 1:
			# Remove and return the only item.
			return self.items.pop()
		assert self.size() > 1
		min_item = self.items[0]
		# Move the last item to the root.
		# Then bubble down to the leaves.
		last_item = self.items.pop()
		self.items[0] = last_item
		if self.size() > 1:
			self._bubble_down(0)
		return min_item

	def replace_min(self, item):
		'''
		Remove and return the minimum item at the root of
		this heap, and insert the given item into this heap.
		This method is more efficient than calling
		delete_min and then insert.
		==TODO==
		Best case running time: ??? under what conditions?
		==TODO==
		Worst case running time: ??? under what conditions?
		'''
		if self.size() == 0:
			raise ValueError(
				'Heap is empty and has no minimum item'
			)
		assert self.size() > 0
		min_item = self.items[0]
		# Replace the root and bubble down to the leaves.
		self.items[0] = item
		if self.size() > 1:
			self._bubble_down(0)
		return min_item

	def _bubble_up(self, index):
		'''
		Ensure the heap ordering property is true above
		the given index, swapping out of order items,
		or until the root node is reached.
		Best case running time: O(1)
		if parent item is smaller than this item.
		Worst case running time: O(log(n))
		if items on path up to root node aren't in order.
		Maximum path length in complete binary tree is log n.
		'''
		if index == 0:
			# This index is the root node.
			# It does not have a parent.
			return

		if not (0 <= index <= self._last_index()):
			raise IndexError(f'Invalid index: {index}')

		# Get the item's value.
		item = self.items[index]

		# Get the parent's index and value.
		parent_index = self._parent_index(index)
		parent_item = self.items[parent_index]

		# If values are out of order,
		# swap this item with parent item.
		if item < parent_item:
			self.items[parent_index] = item
			self.items[index] = parent_item
			# Recursively bubble up again if necessary.
			self._bubble_up(parent_index)

	def _bubble_down(self, index):
		'''
		Ensure the heap ordering property is true below the
		given index, swapping out of order items, or until
		a leaf node is reached.
		Best case running time: O(1)
		if item is smaller than both child items.
		Worst case running time: O(log(n))
		if items on path down to a leaf are out of order.
		Maximum path length in complete binary tree is log n.
		'''
		if not (0 <= index <= self._last_index()):
			raise IndexError(f'Invalid index: {index}')
		# Get the index of the item's left and right children.
		left_index = self._left_child_index(index)
		right_index = self._right_child_index(index)

		if left_index > self._last_index():
			# This index is a leaf node.
			# It does not have any children.
			return
		else:
			# The left item exists.
			left_item = self.items[left_index]

		if right_index > self._last_index():
			# This index has only one child.
			# A rarity, but it happens.
			right_item = None
		else:
			# The right item exists.
			right_item = self.items[right_index]

		# Get the item's value.
		item = self.items[index]

		# Determine which child item
		# to compare this node's item to.
		if right_item is None:
			child_index = left_index
		elif left_item > right_item:
			child_index = right_index
		else:
			child_index = left_index

		# Get the child item's value.
		child_item = self.items[child_index]

		# If values are out of order,
		# swap this item with the child item.
		if child_item < item:
			self.items[index] = child_item
			self.items[child_index] = item
			# Recursively bubble down again if necessary.
			self._bubble_down(child_index)

	def _last_index(self):
		'''
		Return the last valid index
		in the underlying array of items.
		'''
		return len(self.items) - 1

	def _parent_index(self, index):
		'''
		Return the parent index
		of the item at the given index.
		'''
		if index <= 0:
			raise IndexError(
				f'Heap index {index} has no parent index'
			)
		return (index - 1) >> 1 # Shift right to divide by 2

	def _left_child_index(self, index):
		'''
		Return the left child index
		of the item at the given index.
		'''
		return (index << 1) + 1 # Shift left to multiply by 2

	def _right_child_index(self, index):
		'''
		Return the right child index
		of the item at the given index.
		'''
		return (index << 1) + 2 # Shift left to multiply by 2


def test_binary_min_heap():
	# Create a binary min heap of 7 items.
	items = [9, 25, 86, 3, 29, 5, 55]
	heap = BinaryMinHeap()
	print(f'heap: {heap}')

	print('\nInserting items:')
	for index, item in enumerate(items):
		heap.insert(item)
		print(f'insert({item})')
		print(f'heap: {heap}')
		print(f'size: {heap.size()}')
		heap_min = heap.get_min()
		real_min = min(items[: index + 1])
		correct = heap_min == real_min
		print(f'get_min: {heap_min}, correct: {correct}')

	print('\nDeleting items:')
	for item in sorted(items):
		heap_min = heap.delete_min()
		print(f'delete_min: {heap_min}')
		print(f'heap: {heap}')
		print(f'size: {heap.size()}')


if __name__ == '__main__':
	test_binary_min_heap()
