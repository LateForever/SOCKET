# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import socket as s
HOST = s.gethostname()
PORT = 40873

CLIENT = s.socket(s.AF_INET, s.SOCK_STREAM)
CLIENT.connect((HOST, PORT))

def recv(conn):
    msg = b''
    while b'\r\n\r\n' not in msg:
        data = conn.recv(1)
        msg += data
    return msg


while True:
    
    command = input('>> ')
    command = command + '\r\n\r\n'
    CLIENT.sendall(command.encode())
    server_res = recv(CLIENT)
    msg = server_res.decode()
    
    print(msg)
    
    if msg == 'closing-connection':
        CLIENT.close()
        break