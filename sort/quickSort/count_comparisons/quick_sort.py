import random

total_comparasions = 0

def quick_sort(lst):
	return quick_sort_helper(lst, 0, len(lst) -1)

def quick_sort_helper(lst, left, right):
	if left < right:
		pivot = partition(lst, left, right)

		global total_comparasions
		total_comparasions += (right - left)

		quick_sort_helper(lst, left, pivot - 1)
		quick_sort_helper(lst, pivot + 1, right)

	return lst, total_comparasions


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


def test_algorithms ():
	lst = []
	with open('QuickSort.txt') as f:
		lst = [int(i) 	for i in f.readlines()]

	ordered, comparasions = quick_sort(lst)

	print "Number of comparasions -> ", comparasions

test_algorithms()
