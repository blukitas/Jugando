package main

import "fmt"

func mapExample() {
	// Maps associative data type (hashes or dicts in other languages)
	// Map en una linea
	// n := map[string]int{"foo": 1, "bar": 2}

	m := make(map[string]int)
	m["k1"] = 7

	fmt.Println("map:", m)

	// Devolver valor para una clave
	v1 := m["k1"]
	fmt.Println("v1: ", v1)
	fmt.Println("len:", len(m))

	// Borrar
	delete(m, "k1")

	// Pa saber si hay valor en esa clave o no
	_, prs := m["k2"]
	fmt.Println("prs:", prs)

	m["k2"] = 100
	_, prs = m["k2"]
	fmt.Println("prs:", prs)
}
