package main

import (
	"fmt"
)

func binary_search(values_slice []int, value int) bool {
	start := 0
	end := len(values_slice) - 1

	for start <= end {
		mid := (end + start) / 2

		if values_slice[mid] == value {
			return true
		} else if values_slice[mid] > value {
			end = mid - 1
		} else {
			start = mid + 1
		}
	}

	return false
}

func main() {
	values := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
	fmt.Println(binary_search(values, 8))
}
