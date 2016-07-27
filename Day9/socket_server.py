#!/usr/bin/env python
#coding:utf-8
#Author Zhang Shijie
#买手机
import  socket
import  subprocess
ip_port=("127.0.0.1",9999)
#开机
s=socket.socket()
#买手机卡
s.bind(ip_port)
#开机
s.listen(5)
#等待电话，conn是客户端与服务器的连接链路信息
while True:
    conn,addr=s.accept()
    #接受消息
    while  True:
        try:
            recv_data=conn.recv(1024)
            if len(recv_data) == 0:
                break
            #print(recv_data,"resv_data")
            #发消息
            p=subprocess.Popen(str(recv_data,encoding="utf8"),shell=True,stdout=subprocess.PIPE)
            res=p.stdout.read()
            if len(res) == 0:
                send_data="cmd error"
            else:
                send_data=str(res,encoding="gbk")

            send_data=bytes(send_data,encoding="utf8")
            ready_tag="Ready|%s" %len(send_data)
            conn.send(bytes(ready_tag,encoding="utf8"))
            feedback=conn.recv(1024)
            feedback=str(feedback,encoding="utf8")

            if feedback.startswith("Start"):
                conn.send(send_data)
        except Exception:
            break
    #挂电话
    conn.close()