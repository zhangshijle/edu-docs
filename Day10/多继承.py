#!/usr/bin/env python
#coding:utf-8
#Author Zhang Shijie

class A:
    def f1(self):
        print("A")

class B(A):
    def f1(self):
        print("B")

class C(A):
    def f1(self):
        print("C")

class D:
    def f1(self):
        print(D)

class  E(D):
    def f1(self):
        print("E")
class  F(E,D):
    def f2(self):
        print("F")
obj=F.f1()


