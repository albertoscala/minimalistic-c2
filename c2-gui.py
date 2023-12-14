from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

HOST = "localhost"
PORT_HTTP_CLIENT = 8080

clients = []

# Define the dynamic html function
def dynamic_html(path):
    return path[1:] not in clients
        

# Define the request handler class
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # read the top html file
            with open("homepage/hp-top.html", "r") as f:
                tp_html = f.read()

            # read the bottom html file
            with open("homepage/hp-bttm.html", "r") as f:
                bt_html = f.read()
            
            # make get http request to the server to get the clients list
            clients = requests.get("http://localhost:8880/clients").json()

            # create the html elements for the clients list
            clients_html = ""
            for client in clients:
                clients_html += f'<li class="list-group-item"><a href="/{client}">{client}</a></li>'

            # join all the html file parts
            html = tp_html + clients_html + bt_html

            # send the html file to the client
            self.wfile.write(html.encode())
        elif dynamic_html(self.path):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # read the top html file
            with open("console/part1.html", "r") as f:
                tp_html = f.read()

            # read the bottom html file
            with open("console/part2.html", "r") as f:
                bt_html = f.read()
            
            socket_id = self.path[1:]
            
            # join all the html file parts
            html = tp_html + socket_id + bt_html

            # send the html file to the client
            self.wfile.write(html.encode())


if __name__ == "__main__":
    # Create an HTTP server instance
    server = HTTPServer((HOST, PORT_HTTP_CLIENT), MyRequestHandler)

    # Start the server
    server.serve_forever()    