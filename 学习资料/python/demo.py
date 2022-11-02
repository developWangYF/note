#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# a = 'ABC'
# b = a
# a = '王云飞'
# print(a[0])
from copy import copy
from copy import deepcopy
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
# s ='asdaf'
# print(s.lower())
# a=[int(x) for x in input() if x is not ' '] #输入1 2 3
# a,b,c =input() #输入123
# for i in range(1, 4):
#     print(i)
# import sys
# if __name__ == '__main__':
#     print(sys.argv)
#     a=1
#     sys.exit(0)

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#                     _ooOoo_
#                   o8888888o
#                    88" . "88
#                 ( | -  _  - | )
#                     O\ = /O
#                 ____/`---'\____
#                  .' \\| |// `.
#                 / \\|||:|||// \
#               / _|||||-:- |||||- \
#                | | \\\ - /// | |
#              | \_| ''\---/'' | _/ |
#               \ .-\__ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___\_<|>_/___.' >'"".
#       | | : `- \`.;`\  _ /`;.`/ - ` : | |
#          \ \ `-. \_ __\ /__ _/ .-` / /
#      ==`-.____`-.___\_____/___.-`____.-'==
#                     `=---='
'''
@Project ：pythonalgorithms 
@File ：Inversefunction.py
@Author ：不胜人生一场醉@Date ：2021/7/29 23:17 
'''
b=[1]
a=[1,2,b]
c=copy(a)

print(id(b))
print(id(c[2]))
print(a[2])
if a[2] is b:
    print('sss')
elif a[2] == b :
    print('swwww')