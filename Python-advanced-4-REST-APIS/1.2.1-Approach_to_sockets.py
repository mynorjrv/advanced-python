import socket

server_addr = input("What server do you want to connect to? ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET is the socker domain, SOCKET_STREAM is the socket type

# BSD sockets were designed in two domains
# Unix domain - communicate inside the OS
# Internet domain (INET) - communicate via TCP/IP network

# Socket stream represent a character device, it can handle
# individual characters, byte by byte. Ex. a terminal.
# Another option is fixed sized blocks

sock.connect((server_addr, 80))
# 80 is the service number of http
# The form of the target (adress, port number) is specific for INET

http_request = (
    "GET / HTTP/1.1\r\n"
    f"Host: {'www.google.com'}\r\n"
    "Connection: close\r\n"
    "\r\n"
)

# Http request
# GET(Method) /(root document) HTTP/1.1(protocol version)\r\n
# Host: fjdklafjkaf\r\n
# Connection: close(close connection agter serving first request)\r\n
# \r\n(request terminator)

# sock.send(http_request.encode('utf-8'))

sock.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")

reply = sock.recv(10000)
# receives a maximal length of data

sock.shutdown(socket.SHUT_RDWR)
sock.close()
# "We have no more to say to you. 
# We don't want to hear from you, either. 
# The rest is silence."

print(repr(reply))