# automation_x


3、安装robot framework，执行pip install robotframework

4、安装robotframework-ride，执行pip install robotframework-ride
5、安装selenium2library，执行pip install robotframework-selenium2library

6、安装decorator-3.3.3.tar，执行pip install decorator

7、安装selenium，执行pip install selenium


注意：需要在被控机上开启以下服务：
针对winrm service 进行基础配置：
winrm quickconfig

查看winrm service listener:
winrm e winrm/config/listener

为winrm service 配置auth:
winrm set winrm/config/service/auth @{Basic="true"}

为winrm service 配置加密方式为允许非加密：
winrm set winrm/config/service @{AllowUnencrypted="true"}

--open firewall
--网络工作网络

