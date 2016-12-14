"""Client for echo server."""

import socket
import sys


def create_client_socket(message):
    """Function builds the client socket."""
    server_info = socket.getaddrinfo('127.0.0.1', 4001)
    stream_info = [i for i in server_info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    try:
        client.connect(stream_info[-1])
        message += "DISCONNECT"
        client.sendall(message.encode('utf8'))
    except ConnectionRefusedError:
        print("Connection Refused")
    buffer_length = 8
    reply_complete = False
    msg = ''
    while msg[-10:] != "DISCONNECT":
        print("listening")
        msg += client.recv(buffer_length).decode('utf8')
        print("message received")
    print(msg[:-10])
    client.close()

create_client_socket("12345678")


# if __name__ == "__main__":
#     create_client_socket(sys.argv[0])
