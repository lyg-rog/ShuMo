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

#numpy中的常用函数
#计算平方根
# print(np.sqrt(4))
# print(np.sqrt([1,4,9]))
# arr = np.array([1,25,81])
# print(np.sqrt(arr))

#计算指数
# print(np.exp(1))
# print(np.exp(0))

# #计算自然对数
# print(np.log(np.e **2))

#计算正弦值 余弦值
# print(np.sin(1))
# print(np.sin(np.pi/2))
# print(np.cos(np.pi))

#计算绝对值
# arr = np.abs([1,2,-3])
# print(arr)

#计算a的b次幂
# print(np.pow(2,3))

#庆祝codex鼠标卡顿问题得以解决
#四舍五入
# print(np.round([3.2,4.5,8.1,9.7,4.56]))

#向上取整 & 向下取整
# print(np.ceil([1.6,5.1,-2.1,-2.6]))
# print(np.floor([1.6,5.1,-2.1,-2.6]))

#检测缺失值
# print(np.isnan([1,2,3,np.nan,np.nan]))

#求和
# arr = [1,2,3]
# print(np.sum(arr))

#计算平均值
# print(np.mean([1,2,3]))

#计算中位数
# print(np.median([4,1,2]))
# print(np.median([1,2,4,8]))

#方差和标准差
# print(np.var([1,2,3]))
# print(np.std([1,2,3]))
# print(np.sqrt(np.var([1,2,3])))

#计算最大值和最小值
# print(np.max([1,2,3]),np.argmax([1,2,3]))
# print(np.min([1,2,3]),np.argmin([1,2,3]))

#分位数
# print(np.median([1,2,3]))
# print(np.percentile([1,2,3],50))
# print(np.percentile([1,2,3],20)) #1 + 1*0.4 = 1.4
# print(np.percentile([44,47,64,67],25)) #44 + 3*0.75 = 46.25

#累计和 累计积
# arr = np.array([1,2,3])
# print(np.sum(arr))
# print(np.cumsum(arr))
# print(np.cumprod(arr))

# arr = np.array([[1,2,3],[4,5,6]])
# print(np.sum(arr)) #全部加起来的一个标量结果
# print(np.cumsum(arr,axis=1))
# print(np.cumprod(arr,axis=1))

#比较函数
#比较是否大于小于等于
# print(np.greater([3,4,5,6,7],4))
# print(np.less([3,4,5,6,7],4))
# print(np.equal([3,4,5,6,7],4))
# print(np.equal([3,4,5],[4,4,4]))

#逻辑与或非
# print(np.logical_and([0,0],[1,1]))
# print(np.logical_not([0,1]))
# print(np.logical_or([0,0],[1,1]))

#检查数组中是否有一个True
# print(np.any([0,0,0]))
# print(np.all([1,1,1]))

#自定义条件
#print(np.where(条件,符合条件,不符合条件))
# arr = np.array([1,2,3,4,5])
# print(np.where(arr<3,arr,0))

#用于数值的分类
# arr = np.array([1,2,3,4,5])
# print(np.where(arr<3,1,0))

# score = np.random.randint(0,100,20)
# print(score)
# print(np.where(score>=60,'及格','不及格'))
#多分类
# print(np.where(score<60,'不及格',
#                np.where(score<80,'良好','优秀')))

