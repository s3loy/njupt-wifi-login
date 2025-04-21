## njupt-wifi-login

> simply ez login methods 

仅在`windows`系统上使用过，可以自行简单上手修改代码适配()

- 参考了[WiIIiamWei/NJUPT-login: 南京邮电大学校园网登录脚本](https://github.com/WiIIiamWei/NJUPT-login)并在此脚本上进行简化

---



- 目前路由器使用的是[s235784/NJUPT_AutoLogin: 南京邮电大学校园网自动登录脚本，支持Linux（OpenWRT）、Macos、RouterOS平台，内附单线多拨教程](https://github.com/s235784/NJUPT_AutoLogin)诺天学长的脚本

---



## usage

`login.py`的使用见脚本内部，连上网之后使用。

本人做法是先确保运行正常，使用`pyinstaller`打包成`exe`再进行使用

>  `pip install pyinstaller`
>
> `pyinstaller --onefile --icon=favicon.ico login.py`
>
> 当然此处的icon不是必须的，如需要请自行寻找想要迫害的对象。
>
> 应该会有更好的方法出现。

目前使用的时候在~~魔法~~状态仍然可以正常登录

---



`login.bat` 需要把中间的空修改好,原理就是curl一把梭

> 在此作者不知道普通校园网curl指令具体改动，可以补充

此仓库真的只是一个非常无聊的仓库
