import numpy as np
import matplotlib.pyplot as plt

class Kalman(): # 一维kalman滤波
    def __init__(self,x_ini,p_ini,x_now,R):
        self.x_ini = x_ini
        self.x_now = x_now
        self.x_after  = self.X_after()
        self.p_ini = p_ini
        self.p_after = self.P_after()
        self.R = R
        self.kn = self.Kn()
    def kalman(self):
        kn = self.kn
        x_now = self.x_after + kn * (self.x_now - self.x_after)
        p_now = (1 - kn) * self.p_after
        return  x_now ,p_now

    def Kn(self):
        return  self.p_after / (self.p_after + self.R * self.R)
    def X_after(self):
        return self.x_ini
    def P_after(self):
        return self.p_ini

def main():
    np.random.seed(666)
    hight = np.random.normal(50,np.sqrt(5),100) # 随机生成50个数，均值为50，方差为5的随机数 ,用来分析一个房子高度不改变的高度
    x_ini,p_ini,R  = 60 ,225 ,5 #方差为25(标准差为225)，初始标准差为5
    X_now = []
    P_now = []
    for i ,x in enumerate(hight):
        kalman= Kalman(x_ini=x_ini,p_ini=p_ini,x_now=x,R=R)
        x,y  = kalman.kalman()
        x_ini = x
        p_ini = y
        X_now.append(x_ini)
        P_now.append(p_ini)
    plt.plot(np.arange(1, len(hight) + 1),hight,label="measure", color="r")
    plt.plot(np.arange(1, len(hight) + 1),X_now,label="kalman", color="b")
    plt.plot(np.arange(1, len(hight) + 1),np.full(shape=hight.shape,fill_value=50),label="real", color="g")
    plt.legend()
    plt.title("kalman")
    plt.xlabel("times")
    plt.ylabel("high")
    plt.axis([0, len(hight) + 1, 40, 60])
    plt.show()

if __name__ =="__main__":
    main()
