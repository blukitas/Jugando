package main

import "fmt"

// Dos formas de definir, con tipo o señalando que son del mismo tipo
// func plus(a, b int) int {
func plus(a int, b int) int {
	return a + b
}

// Devolver multiples valores
func vals() (int, int) {
	return 3, 7
}

// Funcion con numero arbitrario de parametros.
func sum(nums ...int) {
	fmt.Print(nums, " ")
	total := 0
	for _, num := range nums {
		total += num
	}
	fmt.Println(total)
}

func Funciones() {
	res := plus(1, 2)
	fmt.Println("1+2 =", res)

	a, b := vals()
	fmt.Println(a)
	fmt.Println(b)

	nums := []int{1, 2, 3, 4}
	sum(nums...)
}
