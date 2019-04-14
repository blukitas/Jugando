package main

import "fmt"

func main() {
	// Slices es como las listas u otro tipo más complejo del tipo array,
	// 		que deja hacer operaciones más potentes

	// Crear con make
	// s := make([]string, 3)
	// O sola linea
	s := []string{"g", "h", "i"}

	// Asignar
	s[0] = "a"
	// Agregar 1 o n elementos.
	s = append(s, "e", "f")

	// Copiar
	c := make([]string, len(s))
	copy(c, s)
	fmt.Println("cpy:", c)

	// Slice[low:high]
	l := s[:3]
	fmt.Println("sl2:", l)

	// Multiples dimensiones:
	//     twoD := make([][]int, 3)

}
