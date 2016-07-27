#!/usr/bin/env python
#coding:utf-8
#Author Zhang Shijie
import  socket
ip_port=("127.0.0.1",9999)
s=socket.socket()
s.connect(ip_port)
while 1:
    send_data=input(">>>:").strip()
    if len(send_data) == 0:
        continue
    if send_data == "exit":
        break
    #print(send_data,"send_data")
    s.send(bytes(send_data,encoding="utf8"))
    recv_data = s.recv(1024)
    print(str(recv_data,encoding="utf8"))
s.close()