# 单表查询
## select *, sal*12 as '年薪' from gzt where 条件查询 order by 排序字段名 limit pn，p_size
select 后面跟单个值的时候，生产和表结构相同的一列数据
计算+——*%时如果有null参与结果一定为null


## 条件查询
=	等号，检测两个值是否相等，如果相等返回true	(A = B) 返回false。
<>, !=	不等于，检测两个值是否相等，如果不相等返回true	(A != B) 返回 true。
>，<，>=，<=
区间between and 
查询空值时，条件为is null（不能用 = null）
and or 同时存在时and优先级高，or优先执行可加（）。
in 相当于等多个or      字段名 in（’a‘，‘b’） === 字段名 = ’a‘ or 字段名 = ’b‘  （in不是区间，是单个值）
not in
like 模糊查询 ’%王%‘ _下划线只匹配一个字符。
## 排序
单个字段 order by 字段名 默认升序 asc 降序 decs
多个字段 字段1升序（如果字段1相等，按照字段2降序） order by 字段1 asc，字段2 desc
字段位置排序 order by 2     （第二列排序，不建议在开发中写，因为不健壮，列顺序改变后，要改列号）
## limit 分页
### 注意limit在排序order by 之后执行。
 limit pn，p_size <!-- pn第几页的开始下标 p_size每页数据量   pn= （pn-1）*p_size -->
 limit a  <!-- limit后只有一个数时，表示取前a条数据 -->
## 处理函数
https://www.runoob.com/mysql/mysql-functions.html

### 常用单行处理函数
lower 转换为小写
upper 转换为大写
substr（a，b，c） 取子串    a：被截取字符串 b：起始下标（从1开始，没有0） c：截取的长度
trim 去空格
concat 进行字段字符串拼接
length 去长度
str_to_data 将字符串转换为日期
data_format 格式化日期为字符串
format 设置千分位
round 四舍五入
rand（）生产随机数
ifbull 可以将null转换成一个具体值
now() 系统当前时间 格式为datatime

### 分组函数 多行处理函数
#### 注意：where子句中不能直接使用分组函数
count（）计数
sun（） 求和
avg（） 求平均值
max（） 最大值
min（） 最小值

分组函数计算式主动忽略null，null不参与计算
某个字段的另一个字段最大值（每个部门的最高工资）：select dept,min(sal) from 表名；

# 查询结果去重
select distinct 单个字段 from 表名  单个字段结果去重
select distinct 多个字段 from 表名  多个字段联合去重 
# 多表查询
## 链接查询
 select e.a,d.a from eam e,dept d where e.a = d.a;
### 内连接
 内连接的特点：
 完全能够匹配上这个条件的数据查询出来

 等值链接
 select e.a,d.a from eam e join dept d on e.a = d.a where 查询新生成链接表条件;
 select ... from 链接表名 join 被链接表名 on 链接条件 where 查询条件

 非等值链接
 e数据表 s数据等级范围表(s为范围等级，a为范围最大值，c为范围最小值)
 求每条数据对应等级表

select e.a,e.b，s.s from eam e join dept d on 条件查询(e.sal between d.a and d.c)
 
 自链接：一张表看作两张表
 
 要求得到员工与员工领导姓名表
 
 //eam 员工表 a员工编号 b员工领导编号 c员工名

 select e1.c,e2.c from eam e1 join eam e2 on e1.a = e2.b
### 外连接
 左外连接
  select e.a,d.a from eam e left join dept d on e.a = d.a
 右外连接
  select e.a,d.a from eam e right join dept d on e.a = d.a
 以join右边的表为主表，把主表匹配成功和匹配失败的表都查出来 
### 全连接
### union合并查询结果集
查询句1 union 查询句2
union，进行上下拼接，拼接时要求结果集合并时要求列相同，拼接效率更高
select * from a left join b on a.id = b.id
union
select * from a right join b on a.id = b.id

## 三表/多表链接
 select ... from 
 join b 
 on a和b的链接条件
 join c
 on a和c的链接条件
 join d
 on a和d的链接条件

 ## 子查询（查询子句）
select ... (查询子句1)  from ....(查询子句2) where ...(查询子句3)

查询子句3的查询结果可看作一个值
查询子句2特殊性：查询子句2的查询结果可作为临时表，
查询子句1只能查询出一列数据，按相应条件拼接到主表上。




# insert插入
insert into 表名（字段名1，字段名2，字段名3，字段名4 .....） values（值1，值2，值3，值4.....）
注意：字段名和值一一对应，不可空缺
插入多条记录
insert into 表名（字段名1，字段名2，字段名3，字段名4 .....） values（值1，值2，值3，值4.....），（值1，值2，值3，值4.....），（值1，值2，值3，值4.....）......
# 修改updata
updata 表名 set 字段名1=值1，.... where 条件
注意：如果没有条件的话，会导致数据全部更新。
# 删除数据 delete
delete from 表名 where 条件
注意：如果没有条件会导致整张表所有数据全部删除。
# 事务 
在要求同时执行完一组增添修改删除操作才能进行下一步时，将这组操作封装进一个事务。
一个事务要求，操作全部实现，事务回滚全部给撤销
# 约束条件（在sql文件中编写，或数据库可视化软件进行字段设计时用到）如非空not null 
# 主键 外键
主键只要不重复就行，不需要有意义。
# 索引
字段设置为索引，where条件查询时，若查询条件字段无索引，进行全表扫描；若查询字段有索引，仅扫描索引字段内容查询，从而大大增加查询效率。
## 主键字段自动创建索引，字段有unique约束也会自动创建索引。
可以使用 UNIQUE 约束确保在非主键列中不输入重复的值。
