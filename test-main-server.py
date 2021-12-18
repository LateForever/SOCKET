# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:03:33 2021
@author: alber
"""

import socket as s
HOST = s.gethostname()
PORT = 40872

SERVER_MAIN = s.socket(s.AF_INET, s.SOCK_STREAM)
SERVER_MAIN.bind((HOST, 40872))

SERVER_MAIN.listen(5)

commands = ['login', 'reg', 'exit', 'showall']
server = [[40873, 'proxy']]
        
def recv(conn):
    msg = b''
    while b'\r\n\r\n' not in msg:
        data = conn.recv(1)
        msg += data
    return msg

print('Main Server listening...')

while True:
    conn, addrr = SERVER_MAIN.accept()
    
    print(f"Connected to {addrr}")
    
    msg = recv(conn)
    msg_data = msg.decode()
    print(f'Wiadomosc od Serwera PROXY: {msg_data}')
    
    if msg_data == 'close\r\n\r\n':
        msg_data = 'closing-connection\r\n\r\n'
        conn.sendall(msg_data.encode())
    
    elif msg_data == 'login\r\n\r\n':
        msg_data == 'Podaj login\r\n\r\n'
        conn.sendall(msg_data.encode())
    
    else:
        conn.sendall(msg_data.encode())
    
SERVER_MAIN.close()