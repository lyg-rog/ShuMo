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
np.random.seed(12)
arr = np.random.randint(0,10,(3,4))
print(arr)


