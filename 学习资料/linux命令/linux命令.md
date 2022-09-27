# 参看文件大小
Df命令是Linux查看磁盘空间系统以磁盘分区为单位查看文件系统，可以加上参数查看磁盘剩余空间信息
查看虚拟机内存状态
df -hl
查看Linux目录大小
du -sh /*
查看当前目录下的总大小
du -sh
查看当前目录下的文件大小
du -sh /home/*



要查找使用 netstat 侦听特定端口的进程，请使用以下命令：
```linux
[root@localhost ~]# netstat -anp | grep ":19090"

[root@web ~]# netstat -anp | grep ":19090"
tcp        0      0 127.0.0.1:46278         127.0.0.1:19090         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:46770         127.0.0.1:19090         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:54798         127.0.0.1:19090         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:46484         127.0.0.1:19090         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:44562         127.0.0.1:19090         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:46270         127.0.0.1:19090         TIME_WAIT   -                   
tcp6       0      0 :::19090                :::*                    LISTEN      50848/./api-ztc     
```

# netstat各列数据含义 netstat -natp | grep nginx

列出所有端口netstat -lnp：

1. 关于Proto，Recv-Q，Send-Q等列的具体含义

Proto：协议名

recv-Q：网络接收队列

表示收到的数据已在本地接收缓冲，但是还有多少没有被进程取走，recv()。如果接收队列Recv-Q一直处于阻塞状态，可能是遭受了拒绝服务 denial-of-service 攻击。
send-Q：网路发送队列

对方没有收到的数据或者说没有Ack的,还是本地缓冲区.
如果发送队列Send-Q不能很快的清零，可能是有应用向外发送数据包过快，或者是对方接收数据包不够快。
recv-Q、send-Q这两个值通常应该为0，如果不为0可能是有问题的。packets在两个队列里都不应该有堆积状态。可接受短暂的非0情况。

2. Local Address：本地地址

1) 0.0.0.0:2000：表示监听服务器上所有ip地址的2000端口(0.0.0.0表示本地所有ip)
2) :::2000：也表示监听本地所有ip的2000端口。和 0.0.0.0:2000 的区别是这里表示的是IPv6地址，0.0.0.0表示的是本地所有IPv4地址。
3) ":::" 这三个 : 的前两个 "::" ，是 "0:0:0:0:0:0:0:0" 的缩写，相当于IPv6的 "0.0.0.0" 。表示本机的所有IPv6地址，第三个 : 是IP和端口的分隔符
4) 127.0.0.1:8080：表示监听本机的loopback地址的8080端口。如果某个服务只监听了回环地址，那么只能在本机进行访问，无法通过tcp/ip 协议进行远程访问
5) ::1:9000：表示监听IPv6的回环地址的9000端口，::1这个表示IPv6的loopback地址
3. Foreign Address：外部地址

与本机端口通信的外部socket。显示规则与 Local Address 相同

4. State：状态

链路状态，共有11种。state列共有12中可能的状态，前面11种是按照TCP连接建立的三次握手和TCP连接断开的四次挥手过程来描述的。

状态参数主要有：

1) LISTEN：首先服务端需要打开一个socket进行监听，状态为LISTEN。来自远方TCP端口的连接请求。
2) SYN_SENT：客户端通过应用程序调用connect进行active open。于是客户端tcp发送一个SYN以请求建立一个连接，状态置为SYN_SENT。在发送连接请求后等待匹配的连接请求。
3) SYN_RECV：服务端应发出ACK确认客户端的 SYN，同时自己向客户端发送一个SYN，状态置为SYN_RECV。在收到和发送一个连接请求后等待对连接请求的确认。
4) ESTABLISHED：代表一个打开的连接，双方可以进行或已经在数据交互了。代表一个打开的连接，数据可以传送给用户。
5) FIN-WAIT-1：主动关闭(active close)端应用程序调用close，于是其TCP发出FIN请求主动关闭连接，之后进入FIN_WAIT1状态。等待远程TCP连接中断请求，或先前的连接中断请求的确认。
6) CLOSE-WAIT：被动关闭(passive close)端TCP接到FIN后，就发出ACK以回应FIN请求(它的接收也作为文件结束符传递给上层应用程序)，并进入CLOSE_WAIT。等待从本地用户发来的连接中断请求。
7) FIN-WAIT-2：主动关闭端接到ACK后，就进入了 FIN-WAIT-2。从远程TCP等待连接中断请求。
8) LAST-ACK：被动关闭端一段时间后，接收到文件结束符的应用程序将调用CLOSE关闭连接。这导致它的TCP也发送一个 FIN，等待对方的ACK，这就进入了LAST-ACK。等待原来发向远程TCP的连接中断请求的确认。
9) TIME-WAIT：在主动关闭端接收到FIN后，TCP 就发送ACK包，并进入TIME-WAIT状态。等待足够的时间以确保远程TCP接收到连接中断请求的确认。
10) CLOSING：比较少见。等待远程TCP对连接中断的确认。
11) CLOSED：被动关闭端在接受到ACK包后，就进入了closed的状态。链接结束，没有任何连接状态
12) UNKNOWN：未知的Socket状态
状态参数补充：

SYN：同步序列编号(Synchronize Sequence Numbers)，该标志只在三次握手建立TCP连接时有效，表示一个新的TCP连接请求
ACK：确认编号(Acknowledgement Number)，是对TCP请求的确认标志，同时提示对端系统已成功接收所有数据
FIN：结束标志(Finish)，用来结束一个TCP对话，但对应端口仍处于开放状态，等待接收后续数据
5. PID/Program：

PID即进程id，Program即使用该socket的应用程序



# Linux查看进程号总结 netstat -natp | grep nginx / ps -ef|qrep nginx / lsof -i :80

1. netstat
netstat本身主要是用来查看端口号信息，来判断服务是否启动，输出的信息中也有该进程的 PID号
netstat -natp | grep nginx


2. ss
ss命令显示活动套接字信息，效果与netstat类似，输出信息中也包含了PID号
ss -natp | grep nginx

3. nginx.pid
/usr/local/nginx/logs 目录下存放nginx的正确与错误日志，也包含了nginx的PID号，我们直接查看该文件即可

>cat /usr/local/nginx/logs/nginx.pid


4. ps
ps显示进程状态
ps -ef|qrep nginx
nginx有主进程和工作进程
worker进程用来处理用户连接，master用来管理worker进程（面试常问）


5. lsof
lsof查看文件的进程信息
lsof -i :80
<image src="image/lsof的输出详解.png">

6. top
 top -bc | grep nginx

top命令会不停的刷新，过滤后看一组就行

# kill 杀死进程
在查到端口占用的进程后，如果你要杀掉对应的进程可以使用 kill 命令：

>kill -9 PID

# 解压命令
tar -xzvf file.tar.gz //解压tar.gz