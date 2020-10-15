import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.title(r'$连续时间实指数信号$')

plt.subplot(2, 3, 1)
x = np.linspace(-3, 3, 100)
plt.plot(x, np.exp(x))
y = np.linspace(-3, 3, 100)
plt.plot(y, np.exp(-y))
z = np.linspace(-3, 3, 100)
plt.plot(x, np.exp(z * 0))
plt.title(r'实指数信号')

plt.subplot(2, 3, 2)
h = np.linspace(-3, 3, 100)
plt.plot(x, np.sin(h))
plt.title(r'正弦信号')


def unit(t):
    r = np.where(t > 0.0, 1.0, 0.0)
    return r

plt.subplot(2, 3, 4)
j = np.linspace( -15, 15, 100 )
plt.plot(j, np.exp(0.1*j)*np.cos(3*j))
plt.title('复指数信号')    


plt.subplot(2, 3, 3)
t = np.linspace(-1.0, 3.0, 1000)
plt.ylim(-1.0, 3.0)
plt.xlim(-1, 1)
plt.plot(t, unit(t))
plt.title(r'step signal阶跃信号')



plt.show()

