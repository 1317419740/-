import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t)

def g(t):
    return np.exp(t)

def h(t):
    return np.exp(0*t)

t1 = np.arange(-5.0, 5.0, 0.1)
t2 = np.arange(-5.0, 5.0, 0.1)


plt.figure()            # Called implicitly but can use# for multiple figures
plt.subplot(221)      # 2 rows, 2 column, 1stplot
plt.plot(t1, f(t1), 'b-')
#设置坐标轴范围
plt.xlim((-5, 5))
plt.ylim((-1,10))
#设置坐标轴名称
plt.xlabel('t/s')
plt.ylabel('X(t)')
#设置坐标轴刻度
ax = plt.gca()                                            # get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title("Functional Equation:ω=0,σ=-1,X(t)=e^-t")

plt.subplot(222)      # 2 rows, 2 column, 2ndplot

ax = plt.gca()
plt.plot(t2, g(t2), 'r-')
#设置坐标轴范围
plt.xlim((-5, 5))
plt.ylim((-1, 10))
#设置坐标轴名称
plt.xlabel('t/s')
plt.ylabel('X(t)')
#设置坐标轴刻度
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title("Functional Equation:ω=0,σ=1,X(t)=e^t")

plt.subplot(223)      # 2 rows, 2 column, 3ndplot

ax = plt.gca()
plt.plot(t2, h(t2), 'g-')
#设置坐标轴范围
plt.xlim((-5, 5))
plt.ylim((-1, 10))
#设置坐标轴名称
plt.xlabel('t/s')
plt.ylabel('X(t)')
#设置坐标轴刻度
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bott
ax.spines['left'].set_position(('data', 0))
plt.title("Functional Equation:ω=0,σ=0,X(t)=e^0")


plt.subplot(224)
ax = plt.gca()
plt.plot(t1, f(t1), 'b-')
plt.plot(t2, g(t2), 'r-')
plt.plot(t2, h(t2), 'g-')
plt.xlim((-5, 5))
plt.ylim((-1, 10))
#设置坐标轴名称
plt.xlabel('t/s')
plt.ylabel('X(t)')
#设置坐标轴刻度
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))


plt.show()
