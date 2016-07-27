#!/usr/bin/env python
#coding:utf-8
#Author Zhang Shijie
class Foo:
    def __iter__(self):
        for i in range(1,100):
            yield i
        yield 2

obj =Foo()
for item in obj:
    print(item)