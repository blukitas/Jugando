package main

import "fmt"

// Solo recibe mensajes
func ping(pings chan<- string, msg string) {
	pings <- msg
}

// El primero manda, el segundo recibe
func pong(pings <-chan string, pongs chan<- string) {
	msg := <-pings
	pongs <- msg
}

func channel_direction_example() {
	pings := make(chan string, 1)
	pongs := make(chan string, 1)
	ping(pings, "passed message")
	pong(pings, pongs)
	fmt.Println(<-pongs)
}
