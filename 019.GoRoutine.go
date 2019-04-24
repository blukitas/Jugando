package main

import "fmt"

func f(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}

// A goroutine is a lightweight thread of execution.
func goRoutineExample()) {
	// Thread blocking. Run synchronously
	f("direct")

	// Will execute concurrently with the calling one.
	go f("goroutine")

	// Anonymous function
	go func(msg string) {
		fmt.Println(msg)
	}("going")

	fmt.Scanln()
	fmt.Println("done")
}
