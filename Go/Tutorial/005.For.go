package main

import "fmt"

func ForExample() {
	// Tipo while
	i := 1
	for i <= 3 {
		fmt.Println(i)
		i = i + 1
	}

	// Clasico
	for j := 7; j <= 9; j++ {
		fmt.Println(j)
	}

	// Otro tipo de while
	for {
		fmt.Println("loop")
		break
	}

	// Uso continue
	for n := 0; n <= 5; n++ {
		if n%2 == 0 {
			continue
		}
		fmt.Println(n)
	}
}
