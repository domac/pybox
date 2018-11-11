#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, threading


def connhandle(conn, addr):
    print 'accept a new connect from %s' % str(addr)

    conn.send('Hello')

    while True:
        data = conn.recv(1024)
        if data == 'exit' or not data:
            break
        conn.send('action : %s' % data)

    conn.close()
    print 'connect close from %s .' % str(addr)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 9988))
s.listen(512)

print 'waiting for connection ...'

while True:
    conn, addr = s.accept()
    t = threading.Thread(target=connhandle, args=(conn, addr))
    t.start()
