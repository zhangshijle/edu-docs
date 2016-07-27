#!/usr/bin/env python
#coding:utf-8
#Author Zhang Shijie

class Foo:
    #构造方法
    def __init__(self,name,age):
        self.name=name
        self.age = age

    #析构方法
    def __del__(self):
        pass

    def __call__(self):
        print("call")
    def __str__(self):
        return "%s-->%s" %(self.name,self.age)

    def __getitem__(self, item):
        print(type(item))
        return item

    def __setitem__(self, key, value):
        print(type(key),type(value))

    def __delitem__(self, key):
        print(type(key))

obj = Foo("kkk",10)
ret2 = obj[1:4:2]

obj[1:4]=[11,22,33,44,55]
ret3=obj[3]
print(ret3)

del obj[1:4]