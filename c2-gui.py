from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

HOST = "localhost"
PORT_HTTP_CLIENT = 8080

# Define the request handler class
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        match self.path:
            case "/":
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                # read the top html file
                with open("hp-top.html", "r") as f:
                    tp_html = f.read()

                # read the bottom html file
                with open("hp-bttm.html", "r") as f:
                    bt_html = f.read()
                
                # make get http request to the server to get the clients list
                clients = requests.get("http://localhost:8880/clients").json()

                print(clients)

                # create the html elements for the clients list
                clients_html = ""
                for client in clients:
                    clients_html += f'<li class="list-group-item"><a href="#">{client}</a></li>'

                # join all the html file parts
                html = tp_html + clients_html + bt_html

                # send the html file to the client
                self.wfile.write(html.encode())


if __name__ == "__main__":
    # Create an HTTP server instance
    server = HTTPServer((HOST, PORT_HTTP_CLIENT), MyRequestHandler)

    # Start the server
    server.serve_forever()    