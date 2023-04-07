import numpy as np
import matplotlib.pyplot as plt
import math
class Kalman(): # 简单的一维kalman滤波
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
    np.random.seed(666)
    temperature = np.random.normal(50,np.sqrt(0.1),100) # 随机生成50个数，均值为50，方差为0.1的随机数 ,用来分析一个房子高度不改变的高度
    x_ini,p_ini,R  = 40 ,10000 ,0.1 #（设置的初始数据的标准差可以很大）10000，初始数据的方差为0.1(也就是测量的误差是0.1)
    q = 0.0001 # 加入过程噪声
    X_now = []
    P_now = []
    for i ,x in enumerate(temperature):
        kalman= Kalman(x_ini=x_ini,p_ini=p_ini,x_now=x,R=R,q=q)
        x,y,_ = kalman.kalman()
        x_ini = x
        p_ini = y
        X_now.append(x_ini)
        P_now.append(p_ini)
    plt.plot(np.arange(1, len(temperature) + 1),temperature,label="measure", color="r")
    plt.plot(np.arange(1, len(temperature) + 1),X_now,label="kalman", color="b")
    plt.plot(np.arange(1, len(temperature) + 1),np.full(shape=temperature.shape,fill_value=50),label="real", color="g")
    plt.legend()
    plt.title("kalman")
    plt.xlabel("times")
    plt.ylabel("temperature")
    plt.axis([0, len(temperature) + 1, 49, 51])
    plt.show()

if __name__ =="__main__":
    main()