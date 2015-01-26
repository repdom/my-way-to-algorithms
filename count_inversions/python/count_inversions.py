import operator

def merge_sort(lst, compare = operator.lt):
	if len(lst) < 2:
		return lst[:],0

	middle = len(lst)/2
	left, left_inv = merge_sort(lst[:middle], compare)
	right, right_inv = merge_sort(lst[middle:], compare)

	result, split_inv = merge(left, right, compare)
	return result,(left_inv + right_inv + split_inv)

def merge(left, right, compare):
	result = []
	left_offset = 0
	right_offset = 0
	len_left = len(left)
	len_right = len(right)
	inversions_counter = 0

	while  left_offset < len_left and right_offset < len_right:
		if  compare(left[left_offset], right[right_offset]):
			result.append(left[left_offset])
			left_offset += 1
		else:
			result.append(right[right_offset])
			right_offset += 1
			#inversion -> Number of elemets remaining in the List
			inversions_counter += len(left[left_offset:])

	while left_offset < len_left:
		result.append(left[left_offset])
		left_offset += 1

	while right_offset < len_right:
		result.append(right[right_offset])
		right_offset += 1

	return result,inversions_counter

def test_algorithms (lst, num_inv):
	ordered,inversions = merge_sort(lst)
	assert  inversions == num_inv
	print lst, ": Number of inversions -> ", inversions

test_algorithms([2,3,6,5,1,4], 7)
test_algorithms([1,3,5,2,4, 6], 3)