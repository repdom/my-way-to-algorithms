package main

import (
	"fmt"
	"math/rand"
	"time"
)

func quick_sort(values []int) []int {
	return quick_sort_helper(values, 0, len(values)-1)
}

func quick_sort_helper(values []int, first int, last int) []int {
	if first < last {
		pivot := partition(values, first, last)

		quick_sort_helper(values, first, pivot-1)
		quick_sort_helper(values, pivot+1, last)
	}
	return values
}

func partition(values []int, first int, last int) int {
	pivot_index := choose_pivot(first, last)
	pivot_value := values[pivot_index]

	swap(values, pivot_index, last)
	idx := first
	for index := first; index < last; index++ {
		if values[index] < pivot_value {
			swap(values, idx, index)
			idx += 1
		}
	}
	swap(values, idx, last)
	return idx
}

func choose_pivot(first, last int) int {
	rand.Seed(time.Now().Unix())
	return rand.Intn(last-first+1) + first
}

func swap(L []int, x int, y int) []int {
	L[x], L[y] = L[y], L[x]
	return L
}

func main() {
	a := []int{1, 3, 5, 7, 9, 8, 6, 4, 2}
	fmt.Printf("Unsorted: %v\n", a)
	quick_sort(a)
	fmt.Printf("Sorted: %v\n", a)
}
