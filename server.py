from consts import *
import socket
import json


def server_program():
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(json.loads(data.decode('utf-8')))
        conn.send(json.dumps({"Response": LOGIN_RESPONSE}).encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()