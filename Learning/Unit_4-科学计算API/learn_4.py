#================================================================
# 简单的Numpy程序
#----------------------------------------------------------------
# import numpy as np 

# # 数组
# x1d = np.array([4,23,565])
# print(x1d)
# x2d = np.array(((1,2,3),(4,4,4),(7,7,7)))
# print(x2d)
# x = np.array([4,5,6])
# y = np.array([1,2,3])
# print(x+y)
# print(x*y)
# print(x-y)
# print(x/y)
# print(x%y)

# # matrix子类可进行矩阵运算
# x1 = np.array(((1,2,3),(1,2,3),(1,2,3)))
# x2 = np.array(((1,2,3),(1,2,3),(1,2,3)))
# print('First 2-D Array: x1')
# print(x1)
# print('Second 2-D Array: x2')
# print(x2)
# print('Array Multiplication') # 数组乘法：对应位置上的元素相乘
# print(x1*x2)
# mx1 = np.matrix(((1,2,3),(1,2,3),(1,2,3)))
# mx2 = np.matrix(((1,2,3),(1,2,3),(1,2,3)))
# print('Matrix Multiplication') # 矩阵乘法
# print(mx1*mx2)

# # 简单的统计函数
# xt = np.random.randn(10) # 创建一个有10个随机元素的数组
# print(xt)
# mean = xt.mean()
# print(mean)
# std = xt.std()
# print(std)
# var = xt.var()
# print(var)

#----------------------------------------------------------------


#================================================================
# Scipy做统计 stats.describe
#----------------------------------------------------------------
# import scipy as sp 
# import scipy.stats as st 

# s = sp.randn(10)
# n, min_max, mean, var, skew, kurt = st.describe(s)
# print('Number of elements:', n)
# print('Minimum:', min_max[0], ' Maximum:', min_max[1])
# print('Mean:', mean)
# print('Variance:', var)
# print('Skewness:', skew)
# print('Kurtosis:', kurt)

#----------------------------------------------------------------


#================================================================
# Scipy优化函数    Rosenbrock的非凸函数用于检验优化算法的性能
#----------------------------------------------------------------
# import numpy as np 
# from scipy.optimize import minimize

# # 定义Rosenbrock函数
# def rosenbrock(x):
# 	return sum(100*(x[1:]-x[:-1]**2)**2 + (1-x[:-1])**2)

# x0 = np.array([1, 0.7, 0.8, 2.9, 1.1])
# res = minimize(rosenbrock, x0, method = 'nelder-mead', options = {'xtol':1e-8, 'disp':True})
# print(res.x)

#----------------------------------------------------------------


#================================================================
# Scipy图像处理
#----------------------------------------------------------------
# from scipy import misc
# import matplotlib.pyplot as plt

# # 显示图片
# l = misc.face()
# plt.gray()
# plt.imshow(l)
# plt.show()

#----------------------------------------------------------------


#================================================================
# Scipy图像的几何变换
#----------------------------------------------------------------
# import scipy 
# from scipy import ndimage
# import matplotlib.pyplot as plt
# import numpy as np

# lena = scipy.misc.imread('lena512.bmp')
# lx, ly = lena.shape
# crop_lena = lena[lx//4:-lx//4, ly//4:-ly//4]
# crop_eyes_lena = lena[lx//2:int(-lx/2.2), int(ly//2.1):int(-ly/3.2)]
# rotate_lena = ndimage.rotate(lena, 45)

# # 四幅图 返回二维数组
# f, axarr = plt.subplots(2, 2)
# axarr[0,0].imshow(lena, cmap=plt.cm.gray)
# axarr[0,0].axis('off')
# axarr[0,0].set_title('Original Lena Image')
# axarr[0,1].imshow(crop_lena, cmap=plt.cm.gray)
# axarr[0,1].axis('off')
# axarr[0,1].set_title('Cropped Lena')
# axarr[1,0].imshow(crop_eyes_lena, cmap=plt.cm.gray)
# axarr[1,0].axis('off')
# axarr[1,0].set_title('Lena Cropped Eyes')
# axarr[1,1].imshow(rotate_lena, cmap=plt.cm.gray)
# axarr[1,1].axis('off')
# axarr[1,1].set_title('45 Degree Rotated Lena')

# plt.show() 

#----------------------------------------------------------------


#================================================================
# Sympy 基础符号操作
#----------------------------------------------------------------
# import sympy

# a = sympy.Symbol('a')
# b = sympy.Symbol('b')
# c = sympy.Symbol('c')
# e = (a*b*b+2*b*a*b)+(a*a+c*c)
# print(e)

#----------------------------------------------------------------


#================================================================
# Sympy 表达式拓展
#----------------------------------------------------------------
# import sympy

# a = sympy.Symbol('a')
# b = sympy.Symbol('b')
# e = (a+b)**4
# print(e)
# print(e.expand())
#----------------------------------------------------------------


#================================================================
# Sympy 表达式或公式的简化
#----------------------------------------------------------------
# import sympy
# import math

# x = sympy.Symbol('x')
# a = 1/x+(x*sympy.exp(x)-1)/x
# print(sympy.simplify(a))
# print(sympy.simplify((x**3+x**2-x-1)/(x**2+2*x+1)))
#----------------------------------------------------------------


#================================================================
# Sympy 简单的积分
#----------------------------------------------------------------
# import sympy
# from sympy import integrate

# x = sympy.Symbol('x')
# print(integrate(x**3+2*x**2+x,x))
# print(integrate(x/(x**2+2*x),x))
#----------------------------------------------------------------


#================================================================
# 数据分析和可视化示例
#----------------------------------------------------------------
# import pandas as pd 
# import datetime
# import pandas_datareader.data as pdr
# # 将C:\Users\Administrator\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas_datareader
# # 下的fred.py文件中的pandas.core.common import is_list_like修改为pandas.api.types import is_list_like
# import fix_yahoo_finance as yf

# yf.pdr_override() #需要调用这个函数

# start = datetime.datetime(2014,10,1)
# end = datetime.datetime(2014,12,30)

# apple = pdr.get_data_yahoo('AAPL', start, end)
# print(apple.head())
# apple.to_csv('apple-data.csv')
# df = pd.read_csv('apple-data.csv', index_col='Date', parse_dates=True)
# print(df.head())
#----------------------------------------------------------------


#================================================================
# 二维图像
#----------------------------------------------------------------
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('apple-data.csv', index_col="Date", parse_dates=True)
# df['H-L'] = df.High - df.Low
# df['50MA'] = df['Close'].rolling(50).mean()
# df[['Open','High','Low','Close','50MA']].plot()
# plt.show()
#----------------------------------------------------------------


#================================================================
# 三维图像
#----------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('apple-data.csv', parse_dates=True)
df['H-L'] = df.High - df.Low
df['50MA'] = df['Close'].rolling(50).mean()

threedee = plt.figure().gca(projection='3d')
threedee.scatter(df.index, df['H-L'], df['Close'])
threedee.set_xlabel('Index')
threedee.set_ylabel('H-L')
threedee.set_zlabel('Close')
plt.show()

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


