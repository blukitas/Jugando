package main

import "fmt"

// https://gobyexample.com/closures
// Funcion que devuelve una funcion
func intSeq() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}

func closureExample() {
	nextInt := intSeq()
	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())

	// La funcion arranca con ese i. Cada instancia tiene un estado propio
	newInts := intSeq()
	fmt.Println(newInts())

}
