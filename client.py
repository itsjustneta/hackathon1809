from consts import *
import socket
import json
import ast
import tkinter as tk
from tkinter import *

from server import check_login

global response


def send_to_server(sock, msg):
    sock.send(json.dumps(msg).encode('utf-8'))  # send message
    data = sock.recv(1024).decode()  # receive response

    return ast.literal_eval(data)["Response"]


def show_login_window():
    global response
    response = 0
    window = tk.Tk()
    height = window.winfo_screenheight()
    client_socket = socket.socket()
    client_socket.connect((HOST, PORT))

    def check():
        global response
        username_input, password_input = e1.get(), e2.get()

        msg_dict = {"Id": LOGIN_REQUEST, "Data": f"{username_input}:{password_input}"}
        response = send_to_server(client_socket, msg_dict)
        if response == LOGIN_RESPONSE:
            login_window.quit()
            

    window.destroy()  # closes the previous window
    login_window = Tk()  # creates a new window for loging in
    login_window.title("LogIn")
    login_window.configure(background='lightblue')
    login_window.geometry("%dx%d+0+0" % (400, height))
    # set title to the window
    # add 2 Labels to the window
    username = Label(login_window, text="Username: ", font="times 20", bg='lightblue', fg='darkred')
    username.grid(row=1, column=0)
    password = Label(login_window, text="Password: ", font="times 20", bg='lightblue', fg='darkred')
    password.grid(row=2, column=0)
    l3 = Label(login_window, font="times 20")
    l3.grid(row=5, column=1)
    # creating 2 adjacent text entries
    username_text = StringVar()  # stores string
    e1 = Entry(login_window, textvariable=username_text)
    e1.grid(row=1, column=1)
    password_text = StringVar()
    e2 = Entry(login_window, textvariable=password_text, show='*')
    e2.grid(row=2, column=1)
    # create 1 button to log in
    b = Button(login_window, text="login", width=20, command=check)
    b.grid(row=4, column=1)
    login_window.mainloop()


if __name__ == "__main__":
    show_login_window()
