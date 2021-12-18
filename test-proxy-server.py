# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 19:50:09 2021

@author: alber
"""

import socket as s
HOST = s.gethostname()
PORT = 40873

SERVER = s.socket(s.AF_INET, s.SOCK_STREAM)
SERVER.bind((HOST, PORT))

SERVER.listen(5)
clients = ['albert']
server = [[40872, 'Main']]

print('PROXY Server listening...')

SERVER_MAIN = s.socket(s.AF_INET, s.SOCK_STREAM)

while True:
    conn, addrr = SERVER.accept()
    
    print(f"Connected to {addrr}")
    
    msg = conn.recv(1024)
    msg_data = msg.decode()
    print(msg_data)
    
    print(f'Wiadomosc od klienta: {msg_data}')
    
    SERVER_MAIN.connect((HOST, server[0][0]))
    SERVER_MAIN.sendall(msg_data.encode())
    
    print('cos sie stalo')
    
    while True:
        main_msg = SERVER_MAIN.recv(1024).deocde()
        print('waiting')
        if main_msg != '':
            msg = main_msg
            break
    
    print(f'Wiadomosc od serwera glownego: {msg}')
    conn.sendall(main_msg.encode())
    
SERVER.close()