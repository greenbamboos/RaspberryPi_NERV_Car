###################################################
#               智能小车1.0
#
#               @author Bamboos
#               @date 2019/1/7
###################################################

import threading
import os
from NCode.Modules.WheelModule import *


class NCar:

    def __init__(self):
        # 初始化智能小车使用控制脚--------------
        self.WHEEL_L_IN1 = 11  # 11：左轮
        self.WHEEL_L_IN2 = 12  # 12：左轮
        self.WHEEL_R_IN1 = 13  # 13：右轮
        self.WHEEL_R_IN2 = 15  # 15：右轮
        # 小车状态
        self.status = 'normal'
        self.code = '0'
        # 初始化树莓派gpio控制脚----------------
        # 车轮控制
        self.wheelModule = WheelModule(self.WHEEL_L_IN1, self.WHEEL_L_IN2, self.WHEEL_R_IN1, self.WHEEL_R_IN2)

    # 前进的代码
    def forward(self):
        self.wheelModule.forward()

    # 后退
    def backOff(self):
        self.wheelModule.backOff()

    # 左转
    def leftTurn(self):
        self.wheelModule.leftTurn()

    # 右转
    def rightTurn(self):
        self.wheelModule.rightTurn()

    # 停车
    def stop(self):
        self.wheelModule.stop()
