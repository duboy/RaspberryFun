# RaspberryFun
使用 hcitool & gatttool

安装了bluez协议栈后提供的工具，简单操作如下。

查看蓝牙pc的设备
hcitool dev
1
扫描ble
hcitool lescan
1
设置gatttool
 gatttool  -b 76:66:44:33:22:72 -I
 -I : 进入交互模式

在gatttool下， 
开始连接设备 ： connect 
输入 ： help查看其他指令