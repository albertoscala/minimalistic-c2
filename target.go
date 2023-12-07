package main

import (
	"net"
)

const HOST = "localhost"
const PORT = "8888"

func main() {
	var conn net.Conn // server connection
	var err error     // server connection error

	// connect to the server until there are no errors
	for err != nil {
		conn, err = net.Dial("tcp", HOST+":"+PORT)
	}

	// start infinite loop
	for {
		// listen for the server commands

	}
}
