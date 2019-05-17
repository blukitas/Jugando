package main

import "fmt"

func rangeExample() {
	// Tipo foreach
	// El range da index, value. Se puede usar _ para obviar el que uno no quiera.
	// En caso de map te devuelve (key, value)
	nums := []int{2, 3, 4}
	for i, num := range nums {
		if num == 3 {
			fmt.Println("index:", i)
		}
	}

	// range on strings iterates over Unicode code points.
	// The first value is the starting byte index of the rune and the second the rune itself.
	for i, c := range "go" {
		fmt.Println(i, c)
	}
}
