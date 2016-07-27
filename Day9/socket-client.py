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

    #解决粘包问题
    ready_tag=s.recv(1024)
    ready_tag=str(ready_tag,encoding="utf8")
    if ready_tag.startswith("Ready"): #Ready|1236
        msg_size=int(ready_tag.split("|")[-1])
    start_tag="Start"
    s.send(bytes(start_tag,encoding="utf8"))

    recv_size=0
    recv_msg=b""

    while recv_size < msg_size:
        recv_data = s.recv(1024)
        recv_msg+=recv_data
        recv_size+=len(recv_data)
    print(str(recv_msg,encoding="utf8"))
s.close()