######################################################
#						     #
#           Sort algorithms - MergeSort              #
#						     #
######################################################
import operator

def merge_sort(lst, compare = operator.lt):
	if len(lst) < 2:
		return lst[:]

	middle = len(lst)/2
	left = merge_sort(lst[:middle], compare)
	right = merge_sort(lst[middle:], compare)

	return merge(left, right, compare)

def merge(left, right, compare):
	result = []
	left_offset = 0
	right_offset = 0
	len_left = len(left)
	len_right = len(right)

	while  left_offset < len_left and right_offset < len_right:
	 	if  compare(left[left_offset], right[right_offset]):
	 		result.append(left[left_offset])
	 		left_offset += 1
	 	else:
	 		result.append(right[right_offset])
	 		right_offset += 1

	while left_offset < len_left:
		result.append(left[left_offset])
		left_offset += 1

	while right_offset < len_right:
		result.append(right[right_offset])
		right_offset += 1

	return result

def test_algorithms (sorted, unsorted):
	expected = merge_sort(unsorted)
	assert  expected == sorted
	print unsorted, ": sorted result -> ", expected


test_algorithms([1], [1])
test_algorithms([1, 2], [2, 1])
test_algorithms([1, 2, 3], [2, 3, 1])
test_algorithms([1, 2, 3, 4], [2, 3, 1, 4])
test_algorithms([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 6, 2, 3, 5, 1, 7, 4, 9, 8])
test_algorithms([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 
		[18, 10, 19, 6, 2, 3, 5, 12, 11, 1, 13, 7, 14, 4, 9, 15, 8, 16, 17,20])
