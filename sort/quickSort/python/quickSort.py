import random

def quick_sort(lst):
	return quick_sort_helper(lst, 0, len(lst) -1)

def quick_sort_helper(lst, left, right):
	if left < right:
		pivot = partition(lst, left, right)

		quick_sort_helper(lst, left, pivot - 1)
		quick_sort_helper(lst, pivot + 1, right)

	return lst


def partition(lst, left, right):
	pivot_index = choosePivot_index(left, right)
	pivot = lst[pivot_index]
	# swap pivot and the last element
	swap(lst, right, pivot_index)

	storeidx = left
	for idx in range(left, right):
		if lst[idx] < pivot:
			swap(lst, storeidx, idx)
			storeidx += 1

	# move pivot to the proper position
	swap(lst, storeidx, right)
	return storeidx

def choosePivot_index(start, end):
	return random.randint(start, end)

def swap( L, x, y ):
	L[x], L[y] = L[y], L[x]

def test_algorithms (sorted, unsorted):
	expected = quick_sort(unsorted)
	assert  expected == sorted
	print "sorted result -> ", expected

test_algorithms([1,2,3,4,5,6,7,8,9], [1,3,5,7,9,8,6,4,2])
test_algorithms([1, 2], [2, 1])
test_algorithms([1, 2, 3], [2, 3, 1])
test_algorithms([1, 2, 3, 4], [2, 3, 1, 4])
test_algorithms([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 6, 2, 3, 5, 1, 7, 4, 9, 8])
test_algorithms([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
		[18, 10, 19, 6, 2, 3, 5, 12, 11, 1, 13, 7, 14, 4, 9, 15, 8, 16, 17,20])
