# RaspberryPi_NERV_Car
基于树莓派制作智能小车:H5页面操作移动+实时显示摄像头内容+各类传感器



## 软件环境
> * 烧录系统：RASPBIAN STRETCH  
    需要进行一系列配置，如开启SSH、摄像头、中文设置、更改源等|详情度娘
> * 监控相关：mjpg-streamer
> * 编写语言：Python 3.5
> * 其他使用：Python Flask组件，用于发布小车控制Web服务

## 硬件相关
### 材料
> * 树莓派3代
> * pca9685板子
> * 电机控制板L298N
> * 整流二极管
> * 电阻包
> * 红外避障传感器 
> * 寻迹传感器
> * 超声波传感器
> * 摄像头500w像素（树莓派3代用）
> * 舵机（sg90） 
> * 光敏传感器
> * RGB七彩灯
> * TT马达 
> * 轮胎 
> * 云台 
> * 面包板
> * 0.5A-1A保险丝
> * 四轮智能小车底盘
> * 18650电池组：用于小车供电
> * 充电宝5V2A：用于树莓派供电
> * ......



### 工具
> * 电烙铁
> * 万用表
> * 迷你钻
> * 多头改锥
> * 镊子
> * 剪刀
> * ......

### 耗材/其他
> * 小铜柱
> * 杜邦线
> * M3螺丝
> * 电线
> * 电胶带
> * 双面胶
> * 扎带
> * 开关
> * MicroUsb口的Usb线
> * ......

## 使用介绍
> * 安装 mjpg-streamer 
    <br>
    sudo apt-get -y install subversion libv4l-dev libjpeg8-dev cmake
    <br>
    cd ~
    <br>
    git clone https://github.com/codewithpassion/mjpg-streamer.git
    <br>
    cd mjpg-streamer/mjpg-streamer
    <br>
    sudo make USE_LIBV4L2=true clean all
    <br>
    sudo make DESTDIR=/usr install
    <br>
    也可以直接使用apt install mjpg-streamer 
    <br>
> * 使用 mjpg-streamer 
    <br>
    sudo modprobe bcm2835-v4l2
    <br>
    测试：
    <br>
    mjpg_streamer -i "input_raspicam.so  -fps 15" -o "output_http.so -w /usr/www -p 8080"
    <br>
    在浏览器里面输入 http://192.168.1.1:8080/?action=stream ，应该能看到摄像头抓取的视频.
    
> * 启动小车
    <br>
    shell 下 直接运行 start.sh 或者python3.5(3.0以上本版) python3.5 Start.py
    <br>
    使用前记得将templates 目录下的index.html 中 mjpg_streamer 的ip改成你的树莓派地址
  
###  SHOW
<img src="https://github.com/greenbamboos/RaspberryPi_NERV_Car/blob/master/show/699306985.jpg" width="600" alt="小车照片"/>

<img src="https://github.com/greenbamboos/RaspberryPi_NERV_Car/blob/master/show/2049914867.jpg" width="600" alt="小车照片"/>

