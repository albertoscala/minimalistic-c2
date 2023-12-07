import socket

HOST = "localhost"
PORT = 8888

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
    server_socket.bind((HOST, PORT))

    # listen for connections
    server_socket.listen(1)

    # accept connections
    while True:
        # accept connection
        client_socket, addr = server_socket.accept()

        test_command(client_socket)

        # add client socket to dictionary
        clients_socket[addr] = client_socket


def http_server():
    pass

if __name__ == '__main__':
    tcp_server()