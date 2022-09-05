## xuperchain安装
使用git下载源码到本地

git clone https://github.com/xuperchain/xuperchain.git

执行命令

$ cd xuperchain
$ git checkout -b v5.1.0 v5.1.0
$ make

make 时，可能出现拉取失败的情况，可以配置GOPROXY解决此问题

$ export GOPROXY=https://goproxy.cn,direct
打开你的终端并执行

$ echo "export GO111MODULE=on" >> ~/.profile
$ echo "export GOPROXY=https://goproxy.cn" >> ~/.profile
$ source ~/.profile


## Redis安装
在线安装
直接输入命令 sudo apt-get install redis-server
安装完成后，Redis服务器会自动启动。
使用ps -aux|grep redis命令可以看到服务器系统进程默认端口6379

## 安装 cnpm
1.下载 cnpm
sudo npm install -g cnpm --registry=https://registry.npm.taobao.org
2.创建软链接
sudo ln -s /usr/software/nodejs/bin/cnpm /usr/local/bin
3.查看 cnpm信息
cnpm -v


## 解压zip
unzip s.zip

## 更换用户后git clone 需要用户密码
新增~/.gitconfig文件
vim ~/.gitconfig
写入
[user]
        email = ltby_btxd@163.com
        name = wyf
