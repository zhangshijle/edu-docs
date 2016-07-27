#!/usr/bin/env python
#coding:utf-8
#Author Zhang Shijie

import  socket
import  select
sk = socket.socket()
sk.bind(("127.0.0.1",9991,))
sk.listen(5)

inputs = [sk,]
outputs = []
while True:
    rlist,wlist,e = select.select(inputs,outputs,[],1)
    print(len(inputs),len(rlist),len(wlist),len(outputs))
    for r in rlist:
        if r == sk:
            #print(r)
            conn,address = r.accept()
            inputs.append(conn)
            conn.sendall(bytes("hello",encoding="utf8"))
        else:
            print("=============")
            try:
                data = r.recv(1024)
                if not  data:
                    raise  Exception("断开连接")
                else:
                    print(str(data,encoding="utf-8"))
                    outputs.append(r)
            except Exception as e:
                inputs.remove(r)

    for w in wlist:
        w.sendall(bytes("Response",encoding="utf8"))
        outputs.remove(w)