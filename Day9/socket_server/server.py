#!/usr/bin/env python
#coding:utf-8
#Author Zhang Shijie
import  socketserver
import  subprocess
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall(bytes("欢迎欢迎，热烈欢迎！",encoding="utf8"))
        while True:
            data = self.request.recv(1024)
            if len(data) == 0:break
            print("[%s] says:%s" %(self.client_address,data))
            cmd = subprocess.Popen(data.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            cmd_res = cmd.stdout.read()
            if not cmd_res:
                cmd_res = cmd.stderr.read()
            if len(cmd_res) == 0:
                cmd_res = bytes("cmd has ooutpu",encoding="utf8")

            self.request.send(cmd_res)

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("127.0.0.1",9999),Myserver)
    server.serve_forever()
