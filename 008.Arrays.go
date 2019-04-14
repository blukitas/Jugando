package primerTirito

import "fmt"

func arraysExamples() {

	// Basic array. Fixed length. Zero valued initialized.
	var a [5]int
	fmt.Println("emp:", a)
	// Set
	a[4] = 1020
	fmt.Println("get:", a[4])

	// One-line initialize
	b := [5]int{1, 2, 3, 4, 5}
	fmt.Println("dcl:", b)

	// Multidimentional arrays (As many as needed)
	// Array types are one-dimensional, but you can compose types to build multi-dimensional data structures.
	//var twoD [2][3]int
}
