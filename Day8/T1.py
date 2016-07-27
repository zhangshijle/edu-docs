#!/usr/bin/env python
#coding:utf-8
#Author Zhang Shijie

class Pager:
    def __init__(self,all_count):
        self.all_count = all_count

    @property
    def all_pager(self):
        a1,a2 = divmod(self.all_count,10)
        if a2 == 0:
            return a1
        else:
            return  a1 + 1
    @all_pager.setter
    def all_pager(self,value):
        print(value)

    @all_pager.deleter
    def all_pager(self):
        print("del all_pager")

P = Pager(101)
P.all_pager = 123
#ret = P.all_pager
#print(ret)

del P.all_pager