#!/usr/bin/env python
#coding:utf-8
#Author Zhang Shijie

import  socket
sk = socket.socket()
sk.connect(("127.0.0.1",9991,))
data = sk.recv(1024)
print(data)
while True:
    data = input(">>>")
    sk.sendall(bytes(data,encoding="utf-8"))
sk.close()
