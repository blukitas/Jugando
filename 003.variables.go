package primerTirito

import "fmt"

func variables() {

	var a = "primer variable"
	fmt.Println(a)

	var b, c int = 1, 2
	fmt.Println(b, c)

	var d = true
	fmt.Println(d)

	// Zero valued (En int = 0)
	var e int
	fmt.Println(e)

	// Short way
	f := "short"
	fmt.Println(f)
}
