# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import socket as s

HOST = s.gethostname()
PORT =  3300

server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

while True:
    client, adrr = server_socket.accept()
    welcome_message = adrr, 'Welcome to DarkWeb'
    client.send(str(welcome_message).encode())
    client.close()
    break

server_socket.close()

PORT = 7700

private_server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
private_server_socket.bind((HOST, PORT))
private_server_socket.listen(5)

while True:
    private_client, private_adrr = private_server_socket.accept()
    while True:
        data = private_client.recv(1024)
        received_message = data.decode()
        print(received_message)
        
        if not received_message:
            break
        
        clients_database = ['bitcoinmainer', 'mining123']
        awailable_commands = ['commands', 'EXIT', 'ORDER-TANK', 'LOGIN']
        if received_message not in awailable_commands:
            private_client.send(b'Invalid command')
        
        if received_message == 'commands':
            private_client.send(b'LOGIN, ORDER-TANK, EXIT')
            
        if received_message == 'EXIT':
            private_client.send(b'closing-connection')
            
        if received_message == 'ORDER-TANK':
            private_client.send(b'Chose tank: LEOPARD2, M1-ABRAMS, KONIGSTIGER')
            tank_choose_data = private_client.recv(1024)
            tank_data = tank_choose_data.decode()
            if tank_data == 'LEOPARD2' or 'M1-ABRAMS' or 'KONIGSTIGER':
                private_client.send(b'Please make a 1 bitcoin payment to 3J98tWpEZ73CMnQviecrnyiWrnqRhWNLy')
                bitcoin_payment_data = private_client.recv(1024)
                bitcoin_payment_message = bitcoin_payment_data.decode()
                bitcoin_payment = int(bitcoin_payment_message)
                if bitcoin_payment == 1:
                    private_client.send(b'Thank you for transaction, Tommorow your tank will be in front of your house')
                elif bitcoin_payment > 1:
                    private_client.send(b'You send too much bitcoins they will be returned to your account')
                elif bitcoin_payment < 1:
                    private_client.send(b'You cannot send 0 or -something bitcoins')
                
            else:
                private_client.send(b'You gave wrong tank model')
        
        if received_message == 'LOGIN':
            private_client.send(b'Enter username and password to login into DeepWeeb\nEnter username: ')
            username_received_message = private_client.recv(1024)
            username = username_received_message.decode()
            private_client.send(b'Enter password: ')
            password_received_message = private_client.recv(1024)
            password = password_received_message.decode()
            
            if username == clients_database[0] and password == clients_database[1]:
                private_client.send(b'Welcome into DeepWeb')
            else:
                private_client.send(b'Invalid login or password')
            
         

    
