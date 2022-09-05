# Hyperledger Fabric Node SDK和应用开发
 

Hyperledger Fabric 提供了多种语言的SDK版本，其中提出比较早、比较稳定而全面的是Node.js版本的SDK。

前面提到的fabric示例（如first-network和e2e-cli）都只是在单机上的简单测试，启动一个cli命令行容器来与网络成员节点进行交互，通过在cli容器中手动输入命令完成一系列操作。

而在实际开发中，fabric区块链应用应该拥有一个完整的应用程序来处理前端发起的请求，调用SDK与各节点进行交互，最终利用fabric底层特性将数据存入区块链中。

## 应用模型
在这里插入图片描述

Fabric应用可以分为三层，App层，SDK层，Fabric底层。开发人员需要开发的包括app应用和链码chaincode。应用程序一般运行于客户端节点上，负责处理请求并调用相应SDK与Peer节点，Orderer节点，CA节点进行通信。chiancode负责业务逻辑的执行，从账本查询数据或更新数据到账本。

## Fabric Node SDK主要功能
SDK for Node.js有三个最顶层（top-level）的模块：API, fabric-client 和 fabric-ca-client。具体细节见官方文档及源码。

1. API
该模块给开发者提供了可插拔API，以提供SDK主要接口的可替换实现，包括CryptoSuite, key, KeyValueStore。每个接口都有内置的默认实现。

2. fabric-client
该模块提供了用户客户端与Fabric区块链网络组件（peer，orderer，event等）的交互。主要功能有：

创建channel
发送信息使peer节点加入channel
在peer中安装（install）chaincode
在channel上实例化 chaincode，分为两步：提案（ propose ）和交易（transact）
提交（submit）一个交易（需要调用chaincode），和上面一样分为两步
多种查询功能：状态（通过chaincode），交易，区块，channel，chaincode
监控事件（monitoring events）：包括peer，block，transactions，custom的events
有签名能力的用户对象（ User object）的序列化（serializable）
配置信息的分层（hierarchical configuration settings）
还提供可插拔（pluggable）的日志工具（logging utility）、加密工具（CryptoSuite）和状态存储方法（State Store），可以支持与 peer 或 orderer 的 TLS / non-TLS 链接
3. fabric-ca-client
该模块主要用于成员资格的管理，主要功能如下：

注册（register ）新用户
登录（enroll）用户并且获得由Fabric CA签名（CA私钥完成）的登录证书（enrollment certificate）
通过登录id（enrollment id）来注销 (revoke) 一个用户
可定制的（customizable）持久储存（persistence store）