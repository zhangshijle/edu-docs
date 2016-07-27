#!/usr/bin/env python
#coding:utf-8
#Author Zhang Shijie


class Foo:
    __cc = "123"
    def __init__(self, name):
        self.__name = name

    def f2(self):
        print(self.__name)

    @staticmethod #访问静态字段，只能在内部访问，可以将方法变为静态方法去访问静态字段
    def f3():
        print(Foo.__cc)
obj = Foo("ddd") #访问私有普通字段，只能在方法内部访问
obj.f2()

Foo.f3() #静态方法访问私有静态字段
print(obj._Foo__name)