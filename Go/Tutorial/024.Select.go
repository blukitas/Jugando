package main

import (
	"fmt"
	"time"
)

/*
	The select statement lets a goroutine wait on multiple communication operations.

	A select blocks until one of its cases can run, then it executes that case.
	It chooses one at random if multiple are ready.

*/
func selectExample() {
	// Definicion de los canales
	c1 := make(chan string)
	c2 := make(chan string)

	//Definicion goroutine. Uso el canal
	go func() {
		time.Sleep(1 * time.Second)
		c1 <- "one"
	}()
	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "two"
	}()

	// Dependiendo del mensaje del canal elije
	for i := 0; i < 2; i++ {
		// We’ll use select to await both of these values simultaneously, printing each one as it arrives.
		select {
		case msg1 := <-c1:
			fmt.Println("received", msg1)
		case msg2 := <-c2:
			fmt.Println("received", msg2)
		}
	}
}
