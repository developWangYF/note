![](../../img/git指令.png)

# git  add:将工作区的内容提交的暂存区
# 参看工作区和已暂存文件 git status -s
# 本地连接远程代码仓库
①新建项目目录，进入目录，右键选择  
git bash here    
②初始化git目录   
git init
## ①配置git全局config属性
```
git config --global user.name 'developWangYF' 全局配置用户名           
git config --global user.password '密码' 全局配置密码  
git config --global user.email '----@163.com' 全局配置邮箱  
git config --global core.ignorecase false 设置大小写敏感          

设置不自动转码（很重要，否则windows上传的sh文件在linux里面运 行报错）：
   git config --global core.autocrlf false
   git config --global core.filemode false
   git config --global core.safecrlf true
注：此处可以设置git config 全局配置，只需设置一次，在其他项目中不需要再次设置。
```
## ②本地远程连接github版本库，需根据用户注册邮箱生产ssh私钥
```
ssh-keygen -t rsa -C “blkj@boranet.com.cn”
```
![](../../img/生产gitssh私钥-生产路径在图中.png)
## ③和远程仓库建立连接
git remote add origin 链接地址
## ④拉取项目到本地
git pull origin develop
## ⑤比较本地代码与仓库的区别
git status /git status -s
## ⑥每次提交代码前都要拉取项目到本地
git pull origin 你想要拉取得分支
## ⑦将工作区修改的代码全部提交到暂存区
git add .
## ⑧git commit -m ‘feat(): 增加某某功能’ 本次暂存区提交内容备注
## ⑨将修改提交到远程仓库
git push origin develop 可以指定分支  
注：分支要指定好，一般不提交master分支
<br>
<br>
<br>
<br>

# 远程创建新分支
1. 查看远程和本地的当前分支：git branch -a 、git branch  
2. ①仅创建本地分支  
    ```git
    git branch 新分支名  
    ```
    ②在本地创建新分支并跳转到分支  
    ```git
    git checkout -b develop  
    ```
3. 为远程版本库创建连接  
    ```git
    git push --set-upstream origin develop
    ```
4. 拉取、提交、推送  
    1. git add .     
    2. git  commit -m "备注信息"       
    3. git push origin develop
<br>
<br>
<br>
<br>

# 提交说明
项目一般有3个分支
1. develop用于平常开发代码上传或线上修复bug回传。全新的项目直接上传到develop分支就可以。
2. master用于代码发版时打包的，一般不直接上传代码到master，发版时合并develop中的代码。
3. feature 用于项目迭代，比如一个项目已经发版了，又开了个迭代，新迭代的代码需要上传到feature分支，开发完成后合并到develop分支，再合并到master分支。