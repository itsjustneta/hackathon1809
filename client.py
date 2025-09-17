from consts import *
import socket
import json
import ast


def send_to_server(sock, msg):
    sock.send(json.dumps(msg).encode('utf-8'))  # send message
    data = sock.recv(1024).decode()  # receive response

    return ast.literal_eval(data)["Response"]


def get_username():
    return input("Enter username: ")


def get_password():
    return input("Enter password: ")


def main():
    client_socket = socket.socket()
    client_socket.connect((HOST, PORT))

    response = 0
    while response == ERROR_CODE:
        msg_dict = {"Id": LOGIN_REQUEST, "Data": f"{get_username()}:{get_password()}"}
        response = send_to_server(client_socket, msg_dict)

    client_socket.close()  # close the connection


if __name__ == "__main__":
    main()
