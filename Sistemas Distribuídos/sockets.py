# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import socket 
from datetime import datetime

# BIND
sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
orig = ('localhost', 5000)
sock.bind(orig)
sock.listen(1)

def handle_message(msg):
    if not msg: return 'Ops! Deu ruim'
    cmds = msg.split(' ')
    cmd = msg[0]
    if cmd == 'eco':
        return ''.join(cmds[1:])
    elif cmd == 'soma':
        return sum([int(i) for i in cmds[1:]])
    elif cmd == 'system':
        return datetime.now()
    else:
        return 'Comando inexistente'
    
while True:
    conn, client = sock.accept()
    print('conn, cliente', conn, cliente)
    
    while True:
        msg = conn.recv(1024)
        ret = handle_message(msg)
  
 
 
 
