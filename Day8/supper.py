#!/usr/bin/env python
#coding:utf-8
#Author Zhang Shijie

class C1:
    def f1(self):
        print("c1.f1")
        return  123
class C2(C1):
    def f1(self):
        ret = super(C2,self).f1()
        print("C2.f1")
        return  ret
obj=C2()
obj.f1()