import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

HOST = "localhost"
PORT_TCP = 8888
PORT_HTTP = 8080

clients_socket = dict()

def test_command(client_socket):
    cmd = input("Enter command: ")

    # send the command to the client 
    client_socket.send(cmd.strip().encode())

    # receive the output from the client
    output = client_socket.recv(1024).decode()
    print(output)


def tcp_server():
    # create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind server socket to port
    server_socket.bind((HOST, PORT_TCP))

    # listen for connections
    server_socket.listen(1)

    # accept connections
    while True:
        # accept connection
        client_socket, addr = server_socket.accept()

        # add client socket to dictionary
        clients_socket[addr] = client_socket


# class that models the http server
class HTTPServerStructure(BaseHTTPRequestHandler):
    def do_GET(self):
        match self.path:
            case "/clients":
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write("Test".encode())


def http_server():
    server = HTTPServer((HOST, PORT_HTTP), HTTPServerStructure)
    server.serve_forever()


if __name__ == '__main__':
    # create the tcp server thread
    tcp_server_thread = threading.Thread(target=tcp_server)
    tcp_server_thread.start()

    # create the http server thread
    http_server_thread = threading.Thread(target=http_server)
    http_server_thread.start()

    # wait for the threads to finish
    tcp_server_thread.join()
    http_server_thread.join()