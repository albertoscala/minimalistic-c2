from http.server import BaseHTTPRequestHandler, HTTPServer

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

                # read the html file
                with open("index.html", "r") as file:
                    html = file.read()

                # send the html file to the client
                self.wfile.write(html.encode())


if __name__ == "__main__":
    # Create an HTTP server instance
    server = HTTPServer(('localhost', 8000), MyRequestHandler)

    # Start the server
    server.serve_forever()    