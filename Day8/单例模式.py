#!/usr/bin/env python
#coding:utf-8
#Author Zhang Shijie

class Foo:
    instance = None

    def __init__(self,name):
        self.name = name

    @classmethod
    def get_instance(cls):
        if cls.instance:
            return  cls.instance
        else:
            obj = cls("alc")
            cls.instance = obj
            return  obj
obj1 = Foo.get_instance()
print(obj1)
obj2 = Foo.get_instance()
print(obj2)