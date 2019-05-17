package main

import (
	"fmt"
	"time"
)

/*
	This is the function we’ll run in a goroutine.
		The done channel will be used to notify another
		goroutine that this function’s work is done.
*/
func worker(done chan bool) {
	fmt.Print("working...")
	time.Sleep(time.Second)
	fmt.Println("done")
	done <- true
}

func channelSync() {
	done := make(chan bool, 1)
	go worker(done)
	<-done
}
