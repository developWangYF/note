# Vue配置

## Eslint
ESLint 是一款开源的 JavaScript lint 工具，由 Nicholas C. Zakas 于2013 年创建。

借助 ESLint，可将 静态代码分析 和 问题代码协助修复 集成到 编码、提交 和 打包 过程中，及早发现并协助修复代码中：

有语法错误的部分

不符合约定的样式准则的部分

不符合约定的最佳实践的部分

在项目开发中获得如下收益：

在执行代码之前发现并修复语法错误，减少调试耗时和潜在 bug

保证项目的编码风格统一，提高可维护性

督促团队成员在编码时遵守约定的最佳实践，提高代码质量

总结：ESLint 是一个集代码审查和修复的工具，它的核心功能是通过配置一个个规则来限制代码的合法性和风格

参考：ESLint 官方文档 About 页面 
https://cn.eslint.org/docs/user-guide/getting-started
### 安装eslint
npm i -g eslint
### 配置
如何来配置eslint呢？

1、可以新建一个.eslintrc.*文件，直接创建或者运行eslint --init

2、在package.json文件中使用 eslintConfig 字段指定配置

ESLint 将自动在要检测的文件目录里寻找它们，紧接着是父级目录，一直到文件系统的根目录

ESLint 支持几种格式的配置文件：

JavaScript - 使用 .eslintrc.js 然后输出一个配置对象。

YAML - 使用 .eslintrc.yaml 或 .eslintrc.yml 去定义配置的结构。

JSON - 使用 .eslintrc.json 去定义配置的结构，ESLint 的 JSON 文件允许 JavaScript 风格的注释。

(弃用) - 使用 .eslintrc，可以使 JSON 也可以是 YAML。

package.json - 在 package.json 里创建一个 eslintConfig属性，在那里定义你的配置。

如果同一个目录下有多个配置文件，ESLint 只会使用一个。优先级顺序如下：
.eslintrc.js
.eslintrc.yaml
.eslintrc.yml
.eslintrc.json
.eslintrc
package.json

## EditorConfig插件
EditorConfig帮助开发人员在不同的编辑器和IDE之间定义和维护一致的编码样式。EditorConfig项目由用于定义编码样式的文件格式和一组文本编辑器插件组成，这些插件使编辑器能够读取文件格式并遵循定义的样式。EditorConfig文件易于阅读，并且与版本控制系统配合使用。

不同的开发人员，不同的编辑器，有不同的编码风格，而EditorConfig就是用来协同团队开发人员之间的代码的风格及样式规范化的一个工具，而.editorconfig正是它的默认配置文件。

使用 Eslint 做代码 lint，那么为什么还要使用 .editorconfig 呢？

Eslint 确实包含 .editorconfig 中的一些属性，如缩进等，但并不全部包含，如 .editorconfig 中的 insert_final_newline 属性 Eslint 就没有。Eslint 更偏向于对语法的提示，如定义了一个变量但是没有使用时应该给予提醒。而 .editorconfig 更偏向于代码风格，如缩进等。
Eslint 仅仅支持对 js 文件的校验，而 .editorconfig 不光可以检验 js 文件的代码风格，还可以对 .py（python 文件）、.md（markdown 文件）进行代码风格控制。
总结：根据项目需要，Eslint 和 .editorconfig 并不冲突，同时配合使用可以使代码风格更加优雅。

