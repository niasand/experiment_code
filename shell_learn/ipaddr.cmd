@echo off
 
goto menu
 
:menu
cls
@echo 1. 自动获取ip地址
@echo 2. 手动输入ip地址
@echo 3. 修改DNS
@echo 4. 修改ip为172.16.1.3
@echo 5. 修改ip为188.188.0.9 网关2
@echo 6. 修改ip为172.23.65.13网关1
@echo 7. 查看本机ip地址
@echo 8. 退出
 
@echo.
@echo 默认修改ip为手动输入[直接回车]
@echo.
@echo 请选择
 
set selc=2
set /p selc=
 
@echo.
@echo 正在设置...
@echo.
 
IF %selc%==1 goto DHCP
IF %selc%==2 goto ipsetting 
IF %selc%==3 goto DNS
IF %selc%==4 goto ipstatic2 
IF %selc%==5 goto ipstatic
IF %selc%==6 goto ipstatic1
IF %selc%==7 goto ipconfig
IF %selc%==8 exit
IF %selc% NEQ 8 goto error
exit
 
 
:error
cls
goto menu
exit
 
 
 
:DHCP
@echo.
@echo 自动获取ip地址
netsh int ip set add name="本地连接" source=dhcp
@echo 自动获取DNS服务器
netsh int ip set dns name="本地连接" source=dhcp
@echo 自动获取ip地址设置完毕
@echo.
exit
 
 
 
:ipstatic
@echo.
@echo 设置为188.188.0.9
netsh int ip set add "本地连接" static 188.188.0.9 255.255.0.0 188.188.200.1 1
@echo 正在设置DNS服务器：8.8.8.8
netsh int ip set dns name="本地连接" source=static 8.8.8.8
@echo 静态ip设置完毕
@echo.
exit
 
 
 
:ipstatic1
@echo.
@echo 设置为172.23.65.13
netsh int ip set add "本地连接" static 172.23.65.13 255.255.0.0 172.23.65.244 1
@echo 正在设置DNS服务器：8.8.8.8
netsh int ip set dns name="本地连接" source=static 8.8.8.8
@echo 静态ip设置完毕
@echo.
exit
 
 
 
:ipstatic2
@echo.
@echo 设置为172.16.1.3
netsh int ip set add "本地连接" static 172.16.1.3 255.255.255.0 172.16.1.1 1
@echo 正在设置DNS服务器：8.8.8.8
netsh int ip set dns name="本地连接" source=static 8.8.8.8
@echo 静态ip设置完毕
@echo.
exit
 
 
:ipsetting
cls
@echo.
@echo 正在设置固定ip,请稍候……
@echo.
@echo 请输入ip地址：
set /p ip=
@echo.
@echo 请输入网关：
set /p gw=
@echo.
 
@echo 请输入首选DNS：
set DNS1=8.8.8.8
set /p DNS1=
 
@echo 请输入备用DNS：
set DNS2=8.8.8.8
set /p DNS2=
 
@echo.
netsh interface ip set address 本地连接 source=static addr=%ip% mask=255.255.255.0
netsh interface ip set address name=本地连接 gateway=%gw% gwmetric=1
netsh interface ip set dns 本地连接 static %DNS1%
netsh int ip add dns 本地连接 %DNS2% index=2
@echo ip地址设置完毕
@echo.
exit
 
 
 
 
:DNS
cls
@echo.
@echo 默认设置:首选DNS为8.8.8.8 备用DNS为188.188.200.1
@echo 若修改为默认设置,请直接回车;否则请输入DNS
@echo.
 
@echo 请输入首选DNS：
set DNS1=8.8.8.8
set /p DNS1=
 
@echo 请输入备用DNS：
set DNS2=188.188.200.1
set /p DNS2=
 
@echo.
netsh interface ip set dns 本地连接 static %DNS1%
netsh int ip add dns 本地连接 %DNS2% index=2
@echo DNS设置完毕
@echo.
exit
 
 
:ipconfig
cls
ipconfig /all
@pause
goto menu
exit 
