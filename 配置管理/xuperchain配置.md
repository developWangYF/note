## 智能合约
XuperChain 通过 XuperBridge 实现了合约与虚拟机的解耦，由 XuperBridge 统一进行合约上下文的管理，虚拟机只需要关注无状态的合约执行，从而实现一体化的智能合约引擎。
当前在编程语言方面支持 C++, JAVA, Go, Solidity, 在运行时方面支持 Native 合约，WASM 合约和 EVM 合约。

![语言虚拟机兼容矩阵](../img/语言虚拟机兼容矩阵.png)

### XuperBridge 桥接层
XuperBridge 桥接层实现合约和虚拟机的解耦，桥接层主要负责虚拟机的管理，合约上下文管理，合约执行沙盒，合约代码管理等。
### 智能合约虚拟机



## 合约编写详解

XuperChain目前主要支持以太坊solidity合约，两种编译成wasm格式的合约语言， c++ 和 go，以及两种native合约 go 和 java ，合约框架的整体结构是一致的，在不同语言上的表现形式不太一样，但熟悉一种语言的SDK之后很容易迁移到其他语言。
