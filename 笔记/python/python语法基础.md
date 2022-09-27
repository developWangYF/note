# 常用的数据类型转换 

<image src="image/数据类型转换.png">
 

# 字符串操作

检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1

mystr.find(str, start=0, end=len(mystr))

跟find()方法一样，只不过如果str不在 mystr中会报一个异常. 

mystr.index(str, start=0, end=len(mystr))

'a'是否包含在mystr中，如果是返回开始的索引值，如果否返回
mystr.count('a')

# 切片
切片是指对操作的对象截取其中一部分的操作。字符串、列表、元组都支持切片操作。

切片的语法：[起始:结束:步长]

例:name[0:3] # 取 下标0~2 的字符

# 列表操作

```python
demo:namesList = ['xiaoWang','xiaoZhang','xiaoHua'] 
for name in namesList: 
    print(name)
```

列表中存放的数据是可以进行修改的，比如"增"、"删"、"改""

## '增' 
通过append可以向列表添加元素

> A.append('w')

通过extend可以将另一个集合中的元素逐一添加到列表中(导入集合中所有的子集)

```python
>>> a = [1, 2] 
>>> b = [3, 4] 
>>> a.extend(b) 
>>> a [1, 2, [3, 4], 3, 4]
```

insert(index, object) 在指定位置index前插入元素object

```python
>>> a = [0, 1, 2] 
>>> a.insert(1, 3) 
>>> a [0, 3, 1, 2]
```

## "改"

#修改元素 A[1] = 'xiaoLu'


in, not in 
python中查找的常用方法为：
 in（存在）,如果存在那么结果为true，否则为false 
 not in（不存在），如果不存在那么结果为true，否则false

```python

#查找是否存在 
if findName in nameList: 
    print('在字典中找到了相同的名字') 
else:
    print('没有找到')
```
index、count

index和count与字符串中的用法相同

## "删"

列表元素的常用删除方法有： 
- del：根据下标进行删除 
- pop：删除最后一个元素 
- remove：根据元素的值进行删除

```python
del movieName[2]
movieName.pop()
movieName.remove('列表中值')
```

# 保留字
Ture 和False一定要首字母大写才算是保留字