```python

```

# 返回值：对象遍历
foreach循环用于遍历数组或集合中的元素
与for循环相比，freach 循环不需要获得容器的长度，也不需要根据索引访容器中的元素，但它会自动遍历容器中的每个元素。
```python
# 广泛意义上讲Python语法中本就包含foreach逻辑：
for key, value in d.items():
```

# manage.py命令

manage.py是每个Django项目中自动生成的一个用于管理项目的脚本文件，需要通过python命令执行。manage.py接受的是Django提供的内置命令。

内置命令包含

check #检测全部(或指定)应用常见问题  
dbshell 
diffsettings #显示当前设置文件与Django的默认设置之间的差异。  
flush
makemigrations  #根据检测到的模型创建新的迁移。迁移的作用，更多的是将数据库的操作，以文件的形式记录下来，方便以后检查、调用、重做等等。尤其是对于Git版本管理，它无法获知数据库是如何变化的，只能通过迁移文件中的记录来追溯和保存。 

migrate  #使数据库状态与当前模型集和迁移集同步。说白了，就是将对数据库的更改，主要是数据表设计的更改，在数据库中真实执行。例如，新建、修改、删除数据表，新增、修改、删除某数据表内的字段等等。  
```python
python manage.py makemigrations
python manage.py migrate
```  
runserver #启用Django为我们提供的轻量级的开发用的Web服务器。默认情况下，服务器运行在IP地址127.0.0.1的8000端口上。如果要自定义服务器端口和地址，可以显式地传递一个IP地址和端口号给它。  
shell #启动带有Django环境的Python交互式解释器，也就是命令行环境。默认使用基本的python交互式解释器。这个命令非常常用，是我们测试和开发过程中不可或缺的部分！
startapp #创建新的app。
startproject # 新建工程。默认情况下，新目录包含manage.py脚本和项目包（包含settings.py和其他文件）。
test



# 前端文件生成（vue）

mvnw clean package
# swagger接口问题
```
swagger Unable to render this definition
Unable to render this definition
The provided definition does not specify a valid version field.

Please indicate a valid Swagger or OpenAPI version field. Supported version fields are swagger: "2.0" and those that match openapi: 3.0.n (for example, openapi: 3.0.0).
```
 

可能的原因:  

1、api中的Controller/Action 请加入[HttpPost]或者 [HTTPGet]  

2、api中的Controller中有私有方法（全部写道Service）  

3、传入参数模型有问题.  
