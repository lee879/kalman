import math
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from scipy.linalg import block_diag
# 这是个二维的kalmam滤波
Z = np.arange(1,101) # 观测值
noise = np.random.normal(0,math.sqrt(1),size=Z.shape)
Z = Z + noise # 这里可以理解为一个测量值

#状态 （小车的两个状态都是零）
X = np.array([0,0])
# 状态协方差矩阵，假设这两个状态是相互独立的 各自方差均为1
P = np.array([[1,0],[0,1]])

#状态转移矩阵
F = np.array([[1,1],[0,1]]) # 关于速度和路径的两个矩阵的方程
# 定义状态转移协方差矩阵
Q = np.array([[0.0001,0],[0,0.0001]])# 可以理解为系统产生的误差。传感器的精度

#定义观测矩阵
H = np.array([1,0])
# 定义观测噪声方差(标准差也为1)
R = 1

temp = []
# 开始更新
for i,_ in enumerate(Z):
    # kalman 的5大方程
    X_ = F @ X     # 预测状态 注意这里没有状态控制方程B
    P_ = F @ P @ F.T + Q # 预测状态协方差矩阵
    K = P_ @ H.T / (H @ P_ @ H.T + R)
    X = X_ + K * (Z[i] - H @ X_)
    temp.append(X)
    P = (np.eye(2) - K @ H) * P_

# plt.plot(np.arange(1, len(np.array(temp)[:,0]) + 1), np.array(temp)[:,0], label="s", color="r")
# plt.plot(np.arange(1, len(np.array(temp)[:,1]) + 1), np.array(temp)[:,1], label="v", color="g")
#plt.plot(np.array(temp)[:,0], np.array(temp)[:,1], label="zz", color="b")
plt.scatter(np.array(temp)[:,0], np.array(temp)[:,1],label="staic", color="b")
plt.legend()
plt.title("kalman")
plt.xlabel("V")
plt.ylabel("S")
#plt.axis([0, len(np.array(temp[:,0])) + 1, 40, 60])
plt.show()
