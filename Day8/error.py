#!/usr/bin/env python
#coding:utf-8
#Author Zhang Shijie

while True:
    num1 = input('num1:')
    num2 = input('num2:')
    try:
        li = [1,2,3]
        li[123]
        result = num1 + num2
        print(result)
    except IndexError as a:
        print("index Error")
    except ValueError as a:
        print("Value Error")