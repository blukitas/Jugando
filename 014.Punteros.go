package main

import "fmt"

// Recibe una función (Algo así como ByVal o el parametro más normal de cualquier lenguaje)
func zeroval(ival int) {
	ival = 0
}

// Recibe el puntero (Algo así como el ByRef o el out. Pero muchisimo más flexible)
func zeroptr(iptr *int) {
	*iptr = 0
}

func punterosExample() {
	i := 1
	fmt.Println("initial:", i)
	zeroval(i)
	// No cambia el valor de i
	fmt.Println("zeroval:", i)
	zeroptr(&i)
	// El valor de i muda
	fmt.Println("zeroptr:", i)
	// El print de un puntero es su dirección de memoria
	fmt.Println("pointer:", &i)
	// (Se puede sumar/restar/whateverr a un puntero para moverse como uno quiera?)
}
