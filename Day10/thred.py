#!/usr/bin/env python
#coding:utf-8
#Author Zhang Shijie
import  time
def f1(arg):
    time.sleep(5)
    print(arg)
import  threading
t = threading.Thread(target=f1,args=(123,))
t.setDaemon(True) #表示主线程不等子线程
t.start()  #不代表线程会被立即执行
t.join() #表示主线程到此，当子线程全部执行完成完毕，里面加参数表示最多等几秒
print("end1")
print("end2")
print("end3")
print("end4")
print("end5")