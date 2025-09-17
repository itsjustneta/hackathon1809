from consts import *
import socket
import json
import ast


def check_login(username, password):
    logged_in = False
    with open('accounts.txt') as file:
        for line in file:
            if line.strip().split(',', 1) == [username, password]:
                logged_in = True
    if logged_in:
        return True
    else:
        return False


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

        user_data = json.loads(data.decode('utf-8'))["Data"].split(":")
        print(user_data)

        if check_login(user_data[0], user_data[1]):
            conn.send(json.dumps({"Response": LOGIN_RESPONSE}).encode())  # send data to the client
        else:
            conn.send(json.dumps({"Response": ERROR_CODE}).encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
