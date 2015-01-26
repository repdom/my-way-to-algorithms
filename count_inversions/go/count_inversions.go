package main

import "fmt"

func merge(a []int, b []int) ([]int, int) {
	var result = make([]int, len(a)+len(b))
	var i = 0
	var j = 0
	var num_inversions = 0

	for i < len(a) && j < len(b) {
		if a[i] <= b[j] {
			result[i+j] = a[i]
			i++
		} else {
			result[i+j] = b[j]
			j++
			//inversion -> Number of elemets remaining in the List
			num_inversions = num_inversions + len(a[i:])
		}
	}

	for i < len(a) {
		result[i+j] = a[i]
		i++
	}
	for j < len(b) {
		result[i+j] = b[j]
		j++
	}

	return result, num_inversions
}

func Mergesort(items []int) ([]int, int) {
	if len(items) < 2 {
		return items, 0
	}

	var middle = len(items) / 2

	var a, left_inv = Mergesort(items[:middle])
	var b, right_inv = Mergesort(items[middle:])
	var c, split_inv = merge(a, b)

	return c, (left_inv + right_inv + split_inv)
}

func main() {
	var _, f = Mergesort([]int{2, 3, 6, 5, 1, 4})
	fmt.Print("number of inversions: ", f, "\n")
}
