package main

import (
	"fmt"
)

func binary_search(values []int, key int) bool {
	mid := int(len(values) / 2)

	if len(values) == 0 {
		return false
	}

	if values[mid] == key {
		return true
	} else if values[mid] > key {
		return binary_search(values[:mid], key)
	} else {
		return binary_search(values[mid+1:], key)
	}
}

func main() {
	values := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(values, " has value 3? ", binary_search(values, 3))
	fmt.Println(values, " has value 9? ", binary_search(values, 9))
	fmt.Println(values, " has value 10? ", binary_search(values, 10))
	fmt.Println(values, " has value 12? ", binary_search(values, 12))
	fmt.Println(values, " has value 0? ", binary_search(values, 0))
}
