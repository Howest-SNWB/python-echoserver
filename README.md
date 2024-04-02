# Echo server

Dit eenvoudig Python script wordt gebruikt om een webpagina te tonen aan een client.
_This is a simple Python script that displays HTTP information to a client._

> [!WARNING]
> Not for production use!

## Gebruik / _Usage_

```
usage: echoserver.py [-h] [-p PORT] [-c COLOR]

Echo Server

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Server port number
  -c COLOR, --color COLOR
                        Background color, any CSS color i.e. azure, beige, ...
```
* Port: De poort waarop de server gestart wordt / _The port on which the server will listen_
* Color: De achtergrondkleur van de webpagina / _The backgroundcolor for the webpage_

## Output

```
Echo Server

Request Information

Request: GET / HTTP/1.1 - [02/Apr/2024 18:39:34]
Client: ::1 - 47048

Request Headers

Host: localhost:8080
Connection: keep-alive
sec-ch-ua: "Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,nl-BE;q=0.8,nl;q=0.7

Host Information

Hostname: localhost | FQDN: localhost.localdomain

Server IP: ::1 | Port: 8080

Server: BaseHTTP/0.6 | Version: Python/3.11.8

OS: Linux | Version: Linux-6.8.1-zen1-1-zen-x86_64-with-glibc2.39

Login: username
```
