#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# a = 'ABC'
# b = a
# a = '王云飞'
# print(a[0])
import pickle
import json
# d=dict(name='shirley',age=23,score=98)
# # pickle.dumps()方法： 把任意对象序列化成一个bytes，然后，通过一定方式把这个bytes写入文件。
# print(type(pickle.dumps(d)))

# pickle.dump( )方法： 直接把对象序列化后写入一个file-like Objectimport pickle
# f=open('dump.txt','wb')  #因为序列化之后是bytes，所以是wb
# pickle.dump(d,f)
# f.close()

# d=dict(name='shirley',age=23,score=98)

# print(json.dumps(d)) # 将任意python数据类型转化为str类型

# print(isinstance(json.dumps(d),str)) #判断序列化后的内容类型

# print(type(json.dumps(d)))#判断序列化后的内容类型
# json_str = json.dumps(d)
# print(json.loads(json_str))

# print(type(json.loads(json_str)))

# a = '123456'
# print(a[0:1])# 取一个下标为零的元素
