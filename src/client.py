# -*- coding: utf-8 -*-
"""Client for HTTP server."""

import socket
import sys


def create_client_socket(message):
    """Function builds the client socket."""
    server_info = socket.getaddrinfo('127.0.0.1', 4021)
    stream_info = [i for i in server_info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    try:
        client.connect(stream_info[-1])
        client.sendall(message.encode('utf8'))
    except ConnectionRefusedError:
        print("Connection Refused")
    buffer_length = 8
    msg = b''
    msg_complete = False
    while not msg_complete:
        part = client.recv(buffer_length)
        msg += part
        if len(part) < buffer_length or not part:
            break
    msg = msg.decode('utf8')
    # msg_split = msg.split('\r\n')
    # msg_response = msg.split('\r\n\r\n')[0]
    # msg_body = msg.split('\r\n\r\n')[1]
    # file_type = msg_split[1].split()[1].split('/')[0]
    # if file_type = 'image':

    # print(file_type)
    print(msg)
    client.close()
    return msg


def main():
    """Run create client socket from command line."""
    create_client_socket(sys.argv[1])


if __name__ == "__main__":
    """The script will execute from command line."""
    main()
