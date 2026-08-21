#之前已经写到了160行,接下来继续练习

import numpy as np

#全1
# arr = np.ones((3,4),dtype = int)
# print(arr)

#未初始化
# arr = np.empty((5,4),dtype = int)
# print(arr)

#用指定的数字填充
# arr = np.full((4,4),2026)
# print(arr)

# arr = np.zeros_like(arr)
# print(arr)

# arr = np.ones_like(arr)
# print(arr)
# arr = np.full_like(arr,2025)
# print(arr)

#等差数列
# arr = np.arange(1,10,1)
# print(arr)

# arr = np.arange(1,10,0.1)
# print(arr)

#等间隔数列
# arr = np.linspace(1,10,5)
# print(arr)

#对数间隔数列
# arr = np.logspace(0,4,3,base=2)
# print(arr)

#特殊矩阵的构造
#主对角线上的元素为1,其他的数字为0
# arr = np.eye(3,dtype=int)
# print(arr)

# arr = np.eye(3,4,dtype=int)
# print(arr)

#对角矩阵的构造(主对角线上的元素非0)
# arr = np.diag([1,2,3,4])
# print(arr)

#随机数组的生成
# np.random.seed(12)
# arr = np.random.randint(0,10,(3,4))
# print(arr)

#生成指定范围区间的随机浮点数
# arr = np.random.uniform(3,6,(2,3))
# print(arr)

#生成随机数列(正态分布)
# arr = np.random.randn(2,3)
# print(arr)

#ndarray的数据类型
# arr = np.array([1,0,2,0],dtype = bool)
# print(arr)

#等价于
# arr = np.array([1,0,2,0],dtype = np.bool)
# print(arr)

#索引与切片
# arr = np.random.randint(0,100,20)
# print(arr)
# print(arr[0])
# print(arr[:])
# print(arr[2:5])
# print(arr[slice(2,15,3)])
# print(arr[(arr>10) | (arr<70)])

# arr = np.random.randint(1,100,(4,8))
# print(arr)
# print(arr[1][1])
# print(arr[:,:])
# print(arr[1,2:5])
# print(arr[2,:])
# print(arr[2,:][arr[2,:]>50])
# print(arr[:,3])

#数组与标量之间的运算
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a+3)
# print(a*3)

#广播机制 :1.获取形状 2.是否可以广播
#同一维度 :相同 或者 有一个是1(每一个维度都要求这样)
# a = np.array([1,2,3]) #(1,3)
# b = np.array([[4],[5],[6]]) #(3,1)
# print(a+b)

# #矩阵的乘法
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# b = np.array([[4,5,6],[7,8,9],[1,2,3]])
# print(a*b) #对应位置相乘
# print(a@b) #矩阵乘法
# print(np.matmul(a,b))





