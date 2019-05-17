package main

import "fmt"

type person struct {
	name string
	age  int
}

func structExample() {
	// Omitted fields will be zero-valued.
	s := person{name: "Sean", age: 50}
	fmt.Println(s.name)
	sp := &s
	fmt.Println(sp.age)

	// Structs are mutable.
	sp.age = 51
	fmt.Println(sp.age)

}
