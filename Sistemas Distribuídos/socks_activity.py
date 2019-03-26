# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import socket
from datetime import datetime
from threading import Thread

my_number = 50
my_port = 1518

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = ('localhost', 1518)
sock.bind(orig)
sock.listen(1)

def handle_connection(connection):
        connection.send(my_number.to_bytes(4, byteorder = 'little'))
#       connection.send(bytes(my_number))
#       connection.send(str(my_number).encode('utf-8'))

def run_server():
        while True:
                conn, client = sock.accept()
                print('conn, cliente', conn, client)
                Thread(target = handle_connection, args = (conn, )).start()

Thread(target = run_server).start()
# Thread(target = run_server).start()

def get_number(port):
        try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.connect(('localhost', port))
                        data = s.recv(1024)
                        as_int = int.from_bytes(data, "little")
                        numbers.append(as_int)
                        print("Data is", as_int, "from", port)
        except Exception as e:
                print("Failed: ", port)
                sleep(1)
                get_number(port)
ports = [i for i in range(1512, 1521)]
threads = []
for port in ports:
        if port == my_port: continue
        threads.append(Thread(target = get_number, args = (port, )))
for t in threads:
        t.start()

for t in threads:
        t.join()
print(numbers, sum(numbers))



