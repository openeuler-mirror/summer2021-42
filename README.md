# Summer2021-No.42 支持通过ftrace原始数据分析系统整体的调度latency

#### 介绍
https://gitee.com/openeuler-competition/summer-2021/issues/I3EG0M

#### 软件架构
软件架构说明  
![Image text](https://gitee.com/openeuler-competition/summer2021-42/raw/master/test/framework.png)

#### 安装教程

1. 以openEuler为例，一般现在的linux发行版内核都有配置好的ftrace，可以直接克隆本仓库；否则应先配置ftrace
```
$ git clone https://gitee.com/openeuler-competition/summer2021-42.git 
```
2.  成功更改所在目录，说明安装成功
```
$ cd summer2021-42 
```


#### 使用说明

1.  参考仓库内的test.py，根据自己的需要使用ftrace，然后将输出的原始数据保存到本目录下
```
$ sudo cat /sys/kernel/debug/tracing/trace > trace.log
```
2.  查看系统所有的调度延迟及发生时间点
```
$ python3 tool.py
```
3.  如果想查看更多调度细节
```
$ python3 tool-detailed.py
```

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
