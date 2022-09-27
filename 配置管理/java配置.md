# linux 安装java
## 查找java相关的列表
yum -y list java*
## 安装jdk
yum install java-1.8.0-openjdk.x86_64
## 安装后验证
java -version
## 将jdk的安装路径加入到JAVA_HOME
vi /etc/profile
```
#set java environment
JAVA_HOME=/usr/lib/jvm/jre-1.6.0-openjdk.x86_64
PATH=$PATH:$JAVA_HOME/bin
CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export JAVA_HOME CLASSPATH PATH
```
## 生效环境变量
. /etc/profile （注意 . 之后应有一个空格）
