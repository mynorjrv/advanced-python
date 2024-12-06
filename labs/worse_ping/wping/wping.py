import socket
import sys

import requests

def main():
    if len(sys.argv) == 1:
        print(
            'wping: http server adress is required,\n'
            'port is optional (default=80)'
        )
        exit(1)
    if len(sys.argv) > 3:
        print(
            'wping: accepts 2 arguments: http addres and port\n'
            'more were passed.'
        )
        exit(1)
    port = 80
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[2])
            if port<1 or port>65535:
                raise ValueError
        except ValueError:
            print('wping: invalid port')
            exit(2)

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((sys.argv[1], port))
        sock.send(
            b"HEAD / HTTP/1.1\r\n"
            b"Host: " + bytes(sys.argv[1], "utf8") + b"\r\n"
            b"Connection: close\r\n\r\n"
        )
        reply = sock.recv(1000)
    except socket.timeout:
        print('wping: timeout error')
        exit(3)
    except Exception as e:
        print('wping: exception happend')
        print(e)
        exit(4)
    finally:
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()

    # print(repr(reply))
    # print(type(repr(reply)))
    print(repr(reply).partition('\\r\\n')[0][2:])
    exit(0)