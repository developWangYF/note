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
listeners=PLAINTEXT://内网IP:9092 #云服务器必须设置为内网IP
# kafka的消息存储文件
log.dir=/usr/local/data/kafka‐logs
# kafka 连接 zookeeper 的地址
zookeeper.connect=192.xxx.xx.xx:2181

# 启动服务 , 运行的日志打印在 logs 目录里的server.log 里
# 后台启动，不会打印日志到控制台
1：bin/kafka-server-start.sh -daemon config/server.properties
2：bin/kafka‐server‐start.sh config/server.properties &
bin/kafka-server-start.sh config/server.properties
# 启动成功后,可以进入zookeeper 查看kafka节点
zookeeper/bin/zkCli.sh
ls /

# 停止kafka 
bin/kafka‐server‐stop.sh

```

## 三，Kafka 开启远程连接
确认Linux 防火墙 kafka 的端口已开启，并做下面相关配置

修改配置文件   
vi config/server.properties
advertised.listeners.listeners=PLAINTEXT://外网IP:9092




# 创建kafka第一个消息（单机）
## 创建topic(主题)
bin/kafka-topics.sh --create --bootstrap-server 110.42.193.168:9092 --replication-factor 1 --partitions 1 --topic test
### 查看kafka topic节点
bin/kafka-topics.sh --list --bootstrap-server 110.42.193.168:9092

### 删除topic
 ./bin/kafka-topics.sh  --delete --bootstrap-server 110.42.193.168:9092 --topic kafka1
     此时你若想真正删除它，可以如下操作：

     （1）登录zookeeper客户端：命令：./bin/zookeeper-client

     （2）找到topic所在的目录：ls /brokers/topics

     （3）找到要删除的topic，执行命令：rmr /brokers/topics/【topic name】即可，此时topic被彻底删除。


例如：进入zookeeper安装目录

[apps@localhost zookeeper-3.4.10]$ ./bin/zkCli.sh

...............................................................................

WatchedEvent state:SyncConnected type:None path:null
[zk: localhost:2181(CONNECTED) 0] ls /brokers/topics    #输入  ls /brokers/topics   #指令查看有什么文件

[zk: localhost:2181(CONNECTED) 1] rmr /brokers/topics/要删除的文件名                 #删除完后，quit退出。

最后验证是否删除，也要在另外一台执行zookeeper的 ./bin/zkCli.sh这些操作，进行查看文件是否被删除了ls   /brokers/topics ，

## 创建消费者
bin/kafka-console-consumer.sh --bootstrap-server 110.42.193.168:9092 --topic test --from-beginning  

消费者创建完成之后，因为还没有生产者往topic中发送任何消息，因此这里在执行后没有打印出任何数据  

不过别着急，不要关闭这个终端，打开一个新的终端，接下来创建第一个消息生产者  

## 创建生产者
bin/kafka-console-producer.sh --broker-list 110.42.193.168:9092 --topic test

# 集群kafka
https://blog.csdn.net/weixin_39025362/article/details/106837514

# docker 集群