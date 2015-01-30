def binary_search(lst, value):
	if len(lst) == 0:
		return False
	else:
		mid = len(lst) // 2
		if lst[mid] == value:
			return True
		elif lst[mid] < value:
			return binary_search(lst[mid + 1:], value)
		else:
			return binary_search(lst[:mid], value)

def test_binary_search(lst, value, resp):
	result = binary_search(lst, value)
	assert  result == resp
	if result:
		print lst, ",has value: ", value
	else:
		print lst, ",hasn't value: ", value


test_binary_search([1,2,3,4,5,6,7,8,9], 9, True)
test_binary_search([1,2,3,4,5,6,7,8,9], 2, True)
test_binary_search([1,2,3,4,5,6,7,8,9], 11, False)
test_binary_search([1,2,3,4,5,6,7,8,9], 10, False)

