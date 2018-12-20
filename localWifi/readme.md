# 说明
本项目完成两个功能

1. 插入有线网卡时给树莓派分配一个静态IP:`192.168.202.118`

2. 无线网卡组建一个`192.168.0.1/24` 的无线局域网，对外网封闭，能对连入的设备动态分配IP

# 实现
## 静态IP实现：
> 编辑`/etc/dhcpcd.conf`   
```
interface eth0  
static ip_address=192.168.202.118/24
```
## 无线局域网实现：
> 编辑`/etc/dhcpcd.conf`   
```
interface wlan0  
static ip_address=192.168.0.1/24
```  
>  配置HOSTAPD `/etc/hostapd/hostapd.conf`  
```
interface=wlan0
driver=nl80211
ssid=RaspberryPi
hw_mode=g
channel=6
wmm_enabled=1
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=12345678
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
```

> 制动加载HOSTAPD配置文件 `/etc/default/hostapd`
```
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```