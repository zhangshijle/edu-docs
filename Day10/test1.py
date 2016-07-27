#!/usr/bin/env python
#coding:utf-8
#Author Zhang Shijie


'''
name="jack"

def  f1():
    print(name)
def f2():
    name ="tom"
    return  f1
ret = f2()
ret()
'''




'''
li = [x + 100 for x in range(10) if x > 5]
print(li)
'''
'''

li = [lambda  :[x] for x in range(10)]
for i in li:
    print(i())
'''

li= [lambda :x  for x in range(10)]
for i in li:
    print(i())