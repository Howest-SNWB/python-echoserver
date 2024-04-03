#!/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import socket, os, platform, argparse
from random import choice


def randomColor():
    colors = ['azure', 'beige', 'bisque', 'blanchedalmond', 'burlywood', 'cornsilk', 'gainsboro', 'ghostwhite', 'honeydew', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lemonchiffon', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgrey', 'lightpink', 'lightsalmon', 'lightyellow', 'linen', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'oldlace', 'palegoldenrod', 'papayawhip', 'peachpuff', 'seashell', 'snow', 'thistle', 'wheat', 'whitesmoke']
    return choice(colors)

class HTTPServerV6(HTTPServer):
    address_family = socket.AF_INET6


class customRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Get the hostname and IP address
        host_name = socket.gethostname()
        fqdn = socket.getfqdn(host_name)

        # Get the IPv6 address on which the request was received
        host_socket = self.request.getsockname()

        os_name = platform.system()
        os_version = platform.platform()
        try:
            user_name = os.getlogin()
        except:
            user_name = "SystemD"
        # Create a simple HTML page
        html_content = f"""
        <html>
        <head>
            <title>Echo Server</title>
            <style>
            body {{
                background-color: {background_color};
                font-family: Arial, sans-serif;
            }}
            </style>
        </head>
        <body>
            <h1>Echo Server</h1>
            <h2>Request Information</h2>
            <pre>Request: {self.requestline} - [{self.log_date_time_string()}]</pre>
            <pre>Client: {self.client_address[0]} - {self.client_address[1]}</pre>
            <h3>Request Headers</h3>
            <pre>{self.headers}</pre>
            <h2>Host Information</h2>
            <p>Hostname: <code>{host_name}</code> | FQDN: <code>{fqdn}</code></p>
            <p>Server IP: <code>{host_socket[0]}</code> | Port: <code>{host_socket[1]}</code></p>
            <p>Server: <code>{self.server_version}</code> | Version: <code>{self.sys_version}</code></p>
            <p>OS: <code>{os_name}</code> | Version: <code>{os_version}</code></p>
            <p>Login: <code>{user_name}</code></p>
        </body>
        </html>
        """

        self.wfile.write(bytes(html_content, "utf-8"))

if __name__ == "__main__":
    # Add argument for the port number
    parser = argparse.ArgumentParser(description='Echo Server')
    parser.add_argument('-p', '--port', type=int, default=8080, help='Server port number')
    parser.add_argument('-c', '--color', type=str, default=randomColor(), help='Background color, any CSS color i.e. azure, beige, ...')
    args = parser.parse_args()

    serverPort = args.port

    # Random background color per server
    global background_color 
    background_color = args.color

    # Set the hostname to listen on all interfaces
    hostName = "::"

    webServerV6 = HTTPServerV6((hostName, serverPort), customRequestHandler)
    print(f"Server started at http://[{hostName}]:{serverPort}")
    print("Press ^C to quit")
    print(f"Background color: {background_color}")
    print("! Not for production use !")
    print("="*40)

    try:
        webServerV6.serve_forever()
    except KeyboardInterrupt:
        pass

    webServerV6.server_close()
    print("Server stopped.")
