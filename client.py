#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 20:45:57 2021

@author: akgl
"""

import socket as s

HOST = s.gethostname()
PORT = 3300

client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((HOST, PORT))
first_message = client_socket.recv(1024)
print(first_message)

PORT = 7700

private_client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
private_client_socket.connect((HOST,PORT))

while True:
    command = input('>> ')
    print(command)
    private_client_socket.send(command.encode())
    server_response = private_client_socket.recv(1024)
    print(server_response.decode())
    if server_response.decode() == 'closing-connection':
        break
    
    
    



