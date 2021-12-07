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

while True:
    
    command = input('>> ')
    CLIENT.sendall(command.encode())
    server_res = CLIENT.recv(1024)
    msg = server_res.decode()
    
    print(msg)
    
    if msg == 'closing-connection':
        CLIENT.close()
        break
    
        

    
    






