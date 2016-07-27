#!/usr/bin/env python
#coding:utf-8
#Author Zhang Shijie


class Pager:
    def __init__(self,all_count):
        self.all_count = all_count

    def f1(self):
        return  123

    def f2(self,value):
        print(value)

    def f3(self):
        print("del f3")

    foo = property(fget=f1,fdel=f3,fset=f2)
p = Pager(101)
result = p.foo
print(result)

p.foo = "alex"

del p.foo