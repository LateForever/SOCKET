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

SERVER_PROXY = s.socket(s.AF_INET, s.SOCK_STREAM)

print('Main Server listening...')

while True:
    conn, addrr = SERVER_MAIN.accept()
    
    print(f"Connected to {addrr}")
    
    msg = conn.recv(1024)
    msg_data = msg.decode()
    print(f'Wiadomosc od Serwera PROXY: {msg_data}')
    
    SERVER_PROXY.connect((HOST, server[0][0]))
    
    if msg_data == 'close':
        msg_data = 'closing-connection'
        SERVER_PROXY.sendall(msg_data.encode())
    
    elif msg_data == 'login':
        msg_data == 'Podaj login'
        SERVER_PROXY.sendall(msg_data.encode())
    
    else:
        SERVER_PROXY.sendall(msg_data.encode())
    
SERVER_MAIN.close()
    
    
        
        
    

