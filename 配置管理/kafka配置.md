# Linux 安装 kafka 详细步骤
## 一，kafka 下载地址
http://archive.apache.org/dist/kafka/
## 二，安装步骤
* 2.1 安装JDK (kafka 是Scala 语言开发，运行在 jvm 上)
* 2.2 安装 zookeeper (kafka 依赖 zookeeper)
zookeeper 下载地址：https://zookeeper.apache.org/releases.html
```linux
# 解压文件
tar ‐zxvf apache‐zookeeper‐3.5.8‐bin.tar.gz

# 复制一份配置文件, 方便修改
cp conf/zoo_sample.cfg conf/zoo.cfg

# 启动
bin/zkServer.sh start

# 连接控制台
bin/zkCli.sh 

# 查看zk的根目录相关节点
ls /
```

* 2.3 安装 kafka
kafka 下载地址:http://archive.apache.org/dist/kafka/  
```linux
# 解压 kafka 
tar ‐xzf kafka_2.11‐2.4.1.tgz

# 修改配置文件 
vi config/server.properties

# broker.id属性在kafka集群中必须要是唯一
broker.id=0
# kafka部署的机器ip和提供服务的端口号,切勿设0.0.0.0可能报错
listeners=PLAINTEXT://192.xxx.xx.xx:9092
# kafka的消息存储文件
log.dir=/usr/local/data/kafka‐logs
# kafka 连接 zookeeper 的地址
zookeeper.connect=192.xxx.xx.xx:2181

# 启动服务 , 运行的日志打印在 logs 目录里的server.log 里
# 后台启动，不会打印日志到控制台
1：bin/kafka‐server‐start.sh ‐daemon config/server.properties 
2：bin/kafka‐server‐start.sh config/server.properties &

# 启动成功后,可以进入zookeeper 查看kafka节点
zookeeper/bin/zkCli.sh
ls /

# 停止kafka 
bin/kafka‐server‐stop.sh

```

## 三，Kafka 开启远程连接
确认Linux 防火墙 kafka 的端口已开启，并做下面相关配置
