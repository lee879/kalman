import numpy as np
import matplotlib.pyplot as plt
import math
#滞后误差是一个常数，可以通过过程噪声的增大来处理（如果找不到合理的模型）
class Kalman(): # 一维kalman滤波,预测动态系统
    def __init__(self,x_ini,p_ini,x_now,R,q):
        self.q = q
        self.x_ini = x_ini
        self.x_now = x_now
        self.R = R
        self.p_ini = p_ini

        self.x_after = self.X_after()
        self.p_after = self.P_after()
        self.kn = self.Kn()

    def kalman(self):
        kn = self.kn
        x_now = self.x_after + kn * (self.x_now - self.x_after)
        p_now = (1 - kn) * self.p_after
        print(kn,x_now,p_now)
        return  x_now ,p_now ,kn

    def Kn(self):
        return  math.floor(self.p_after / (self.p_after + self.R * self.R) * 1000000) / 1000000
    def X_after(self):
        return self.x_ini #静态模型
    def P_after(self):
        return self.p_ini + self.q

def main():
   # np.random.seed(666)
    real_temperature = np.array([50.479,51.025,51.5,52.003,52.494,53.002,53.499,54.006,54.498,54.991]) # 真实的温度
    measure_temperature = np.array([50.45,50.967,51.6,52.106,52.492,52.819,53.433,54.007,54.523,54.99]) # 测量的温度
    x_ini,p_ini,R  = 10 ,10000 ,0.1 #（设置的初始数据的标准差可以很大）设置方差为10000，初始数据的标准差为0.1(也就是测量的误差是0.1)
    #q = 0.0001 # 过程噪声
    q = 0.2 # 加入大的过程噪声
    X_now = []
    P_now = []
    for i ,x in enumerate(measure_temperature):
        kalman= Kalman(x_ini=x_ini,p_ini=p_ini,x_now=x,R=R,q=q)
        x,y,_ = kalman.kalman()
        x_ini = x
        p_ini = y
        X_now.append(x_ini)
        P_now.append(p_ini)
    plt.plot(np.arange(1, len(measure_temperature) + 1),measure_temperature,label="measure", color="r",marker='x')
    plt.plot(np.arange(1, len(X_now) + 1),X_now,label="kalman", color="b",marker='o')
    plt.plot(np.arange(1, len(real_temperature) + 1),real_temperature,label="real", color="g",marker='*')
    plt.legend()
    plt.title("kalman")
    plt.xlabel("times")
    plt.ylabel("temperature")
    plt.axis([0, len(X_now) + 1, 47.5, 55.5])
    plt.show()

if __name__ =="__main__":
    main()
