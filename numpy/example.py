from email.policy import default

import numpy as np

# 1.数组的创建
# arr = np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))

# arr = np.array([[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7]])
# print(arr)
# print(type(arr))
# print(arr.shape)

# 2.索引和切片
# print(arr[1])
# print(arr[0:2])
# print(arr[1][2])

# 3.运算 +-*/ 对应位置上的元素进行
# print([1,2,3]+[4,5,6])
# arr = np.array([1,2,3])+np.array([2,3,4])
# print(arr)
# arr_= np.array([1,2,3])*np.array([2,3,4])
# print(arr_)
# arr__= np.array([2,3,4])-np.array([1,2,3])
# print(arr__)
# arr___= np.array([2,4,6])/np.array([1,2,3])
# print(arr___)

# 4.数组形状操作
# arr = np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6]]) #不可以把行分开写
# print(arr.shape)
# print(arr)
# new_arr = arr.reshape(2,6)
# print(new_arr.shape)
# print(new_arr)

#数组的转置:
# arr_transpose = arr.transpose()
# print(arr_transpose.shape)
# print(arr_transpose)

# 5. 进阶 线性代数 统计
#矩阵相乘
# arr1 = np.array([[1,2,3],[4,5,6]])
# arr2 =np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6]])
# mul_arr = arr1@arr2
# print(mul_arr.shape)
# print(mul_arr)

#等价于这种写法
# print(np.matmul(arr1,arr2))

#点积
# arr1 = np.array([1,2,3])
# arr2 = np.array([2,3,4])
# print(np.dot(arr1,arr2))

#平均值 最大值 最小值
# arr = np.array([[1,3,7],[45,2,8],[34,7,9]])
# print(arr)
#
# print("数组的平均值:",arr.mean())
# print("数组中的最大值:",arr.max())
# print("数组中的最小值:",arr.min())
# print("数组的和为",arr.sum())
# print("数组的标准差:",arr.std())
# print("数组的排序:",np.sort(arr))
# print("将数组变成一行后再进行排序",np.sort(arr.reshape(-1)))
# print(arr<10) #输出对应数组位置的true false数组
# print(arr[arr<10])
# print(arr[(arr<10) & (arr>2)])
# print(arr[(arr<10) | (arr>10)])

# 保存和导入
#npy
# np.save("arr",arr)
# arr = np.load("arr.npy")
# print(arr)

# 练习:生成随机的4*4数组 筛选10以内的数 并且计算所有数字的和
# arr = np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]])
# print("所有元素的和", arr.sum())
# print("所有10以内的数:",arr[arr<10])

# np.random.seed(12)
# flo_num = np.random.rand()
# int_num = np.random.randint(0,100,1)
# print(flo_num,int_num)
# arr = np.random.randint(0,100,size=(4,4)) #等价于 arr = np.random.randint(0,100,16).reshape(4,4)
# print(arr)
# print("所有元素的和", arr.sum())
# print("所有10以内的数:",arr[arr<=10])


#二次学习
#ndarray特性:
#多维性
# arr = np.array(5) #创建一个0维
# print(arr)
# print(type(arr))
# print(arr.ndim) #证明创建了一个0维度的数组
#
# arr1 = np.array([1,2,3])
# print(arr1) #打印出来的格式中不带逗号
# print(arr1.ndim)
#
# arr2 = np.array([[1,2,3],[4,5,6]])
# print(arr2)
# print(arr2.ndim)

#同质性
# arr = np.array([1,'hello'])
# print(arr) #同质化处理,使得更多性质被保留

# arr1 = np.array([1,2.5])
# print(arr1)#同质化处理
# print(type(arr1[0]))

#高效性

# #ndarray的属性
# arr= np.array([1,2,3])
# print(arr.shape )
# print(arr.ndim)
# print(arr.size)
# print(arr.dtype)
# print(arr.T)
#
# arr1 = np.array([[1,2,3],[4,5,6]])
# print(arr1.shape)
# print(arr1.size) #注意输出是6,即行数乘以列数
# print(arr1)
# print(arr1.T)

#ndarray的创建
#基础的创建方法
# arr = np.array([1,2,3])
# print(arr)

# list1 = [4,5,6]
# arr = np.array(list1,dtype=np.float64)
# print(arr)

#copy
# arr1 = np.copy(arr) # 元素跟原始的数组相同,但是不是一个数组了
# print(arr1)

#预定义形状
#全0
# arr = np.zeros((2,3),dtype = int)
# print(arr)
# print(arr.dtype)

# arr1 = np.zeros((18,),dtype = int)
# print(arr1)

#全1
# arr = np.ones((5,4),dtype = int)
# print(arr)

#未初始化
# arr = np.empty((5,4))
# print(arr)

#用指定的数字填充
# arr = np.full((4,4),2026)
# print(arr)
#
# arr1 = np.zeros_like(arr)
# print(arr1)
# arr1 = np.ones_like(arr)
# print(arr1)
# arr1 = np.empty_like(arr)
# print(arr1)
# arr1 = np.full_like(arr,2027)
# print(arr1)

#等差数列
# arr = np.arange(1,10,1) #(start,end,step) [start,end) 左闭右开区间
# print(arr)

# arr1 = np.arange(2,11,2) #1-10的偶数
# print(arr1)

#等间隔数列
# app = np.linspace(1,10,5)
# print(app)
#应用场景(给0到100分成4个等级,也就是5个节点分数)
# level = np.linspace(0,100,5)
# print(level)

#对数间隔数列
# arr = np.logspace(0,4,3,base=2) #参数为(start , end ,等分点个数 ,指数底数)
# print(arr)

#特殊矩阵的构造
#主对角线上的元素为1,其他的数字为0
# arr = np.eye(3,dtype=int) #3行3列
# print(arr)
#
# arr = np.eye(3,4,dtype=int)
# print(arr)

#对角矩阵的构造(主对角线上的元素非0)
# arr = np.diag([1,2,3,4])
# print(arr)

#随机数组的生成
# np.random.seed(12)
# arr = np.random.rand(2,3)
# print(arr)

#生成指定范围区间的随机浮点数
# arr = np.random.uniform(3,6,(2,3))
# print(arr)

#生成指定范围区间的随机整数
# arr = np.random.randint(3,30,(2,3))
# print(arr)

#生成随机数列(正态分布)
# arr = np.random.randn(2,3)
# print(arr)

#设置随机种子
# np.random.seed(42)
# arr = np.random.randint(1,10,(2,5))
# print(arr)

#ndarray的数据类型
# arr =np.array([1,0,2,0],dtype = 'bool') #非0为true , 0为false
#等价于
# arr =np.array([1,0,2,0],dtype = np.bool)

# arr =np.array([1,0,127,0],dtype = np.int8)
# print(arr)

#索引与切片
#一维数组
# arr = np.random.randint(1,100,20)
# print(arr)
#
# print(arr[0])
# print(arr[:]) #获取全部的数据
# print(arr[2:5]) #获取到左闭右开区间
# print(arr[slice(2,15,3)]) # start end step是冒号方法的等价写法
# print(arr[(arr>10) | (arr<70)]) # 布尔索引

#二维数组的索隐与切片
# arr = np.random.randint(1,100,(4,8))
# print(arr)

# print(arr[1][1])
# print(arr[:,:])
# print(arr[1,2:5])
# print(arr[2,:])#行筛选
# print(arr[2,:][arr[2,:]>50]) #行的二次筛选(选出第3行大于50的数据)
# print(arr[:,3])#列筛选

#ndarray的运算
#算术运算
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(a+b) #对应位相加
# print(a-b) #对应位相减
# print(a*b) #对应位相乘
# print(a/b) #对应位相除
# print(a**2)
#
# c= [1,2,3]
# d= [4,5,6]
# print(c+d) #实现了拼接操作
# #如果列表想要实现对应位相加:使用循环语句
# for i in range(len(d)):
#     c[i] += d[i]
# print(c)

# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# b = np.array([[4,5,6],[7,8,9],[1,2,3]])
# print(a+b) #对应位相加
# print(a-b) #对应位相减
# print(a*b) #对应位相乘
# print(a/b) #对应位相除
# print(a**2)

#数组与标量之间的运算
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a+3)#对每个数字加上3
# print(a*3)

#广播机制 :1.获取形状 2.是否可以广播
#同一维度 :相同 或者 有一个是1(每一个维度都要求这样)
# a = np.array([1,2,3]) #(1,3)
# b = np.array([[4],[5],[6]]) #(3,1)
'''
a的扩充:
1 2 3
1 2 3 
1 2 3

b的扩充:
4 4 4
5 5 5
6 6 6 
然后相加
'''
# print(a+b)

#矩阵的运算
#乘法
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# b = np.array([[4,5,6],[7,8,9],[1,2,3]])
# print(a*b)
# print(a @ b)
# #等价写法如下
# print(np.matmul(a,b))

#numpy中的常用函数
#基本数学函数
#计算平方根(返回浮点数)
# print(np.sqrt(4))
# print(np.sqrt([1,4,9]))
# arr = np.array([1,25,81])
# print(np.sqrt(arr))

#计算指数 (计算 y = e^X)
# print(np.exp(1))
# print(np.exp(0))

#计算自然对数 (计算X =lny)
# print(np.log(np.e ** 2))

#计算正弦值 余弦值
# print(np.sin(1))
# print(np.sin(np.pi/2))
# print(np.cos(np.pi))

#计算绝对值
# arr = np.array([1,-2,3])
# print(np.abs(arr))

#计算a的b次幂
# print(np.pow(2,3))
# print(np.pow(arr,2))

#四舍五入
# print(np.round([3.2,4.5,8.1,9.7])) #4.5会舍去,但是4.5x 会进位为5

#向上取整,向下取整
# arr = np.array([1.6,5.1])
# print(np.ceil(arr))
# print(np.floor(arr))

#检测缺失值NaN
# print(np.isnan([1, 2, np.nan, 3]))

# arr = np.random.randint(1,20,8)
# print(arr)
#
# #求和
# print(np.sum(arr))
# print(np.sum([1,2,3]))

#计算平均值
# print(np.mean([1, 2, 3]))

#计算中位数
# print(np.median([4,1,2])) #median函数先对数组排序,再取中间位置的数
# print(np.median([1,2,4,8]))#中间两个数的平均值

# #计算标准差和方差(反映数值的离散程度)
# print(np.var([1,2,3])) #方差的计算过程:先计算平均值,然后每一项减去平均值平方累加,最后除以数字个数
# print(np.std([1,2,3]))#标准差就是对方差进行开根号处理
# print(np.sqrt(np.var([1, 2, 3])))

#应用(误差的稳定程度)
# arr1 = np.array([1,2,1,2,1,1,1,2])
# arr2 = np.array([1,0,3,0,0,0,4,3])
# print(arr1.mean())
# print(arr1.var())
# print(arr2.mean())
# print(arr2.var())

#计算最大值 最小值
# print(arr1)
# print(np.max(arr1),np.argmax(arr1))
# print(np.min(arr1),np.argmin(arr1))

#分位数
#中位数
# print(np.median([1,2,3]))
# print(np.percentile([1,2,3],20))
# print(np.percentile([44,47,64,67],25))
#-----------------------------------------
#44  1个单位  47   1个单位  64  1个单位    67
#3(单位数) * 0.25 =0.75
#44 + (47-44)*0.75 = 44+3*0.75 =44 + 2.25 =46.25

#累计和 累计积
# arr =np.array([1,2,3])
# print(np.sum(arr))
# print(np.cumsum(arr))
# print(np.cumprod(arr))

#比较函数
#比较是否大于小于等于
#是否大于
# print(np.greater([3,4,5,6,7],4))
#是否小于
# print(np.less([3,4,5,6,7],4))
#是否等于
# print(np.equal([3,4,5,6,7],4))
# print(np.equal([3,4,5],[4,4,4]))

#逻辑与或非
# print(np.logical_and([0,0],[1,1]))
# print(np.logical_not([0,1]))
# print(np.logical_or([0,0],[1,1]))

#检查数组中是否有一个为True,是否所有都为True,自定义条件
#检查数组中是否有一个为True
# print(np.any([0,0,0]))
#检查数组是否都为True
# print(np.all([1,1,1]))

#自定义条件
#print(np.where(条件,符合条件,不符合条件))
# arr = np.array([1,2,3,4,5])
# print(np.where(arr>3,arr,0))

#用于数值的分类
# arr = np.array([1,2,3,4,5])
# print(np.where(arr<3,1,0))

# score = np.random.randint(50,100,20)
# print(score)
# print(np.where(score>=60,'及格','不及格'))

#优化---多分类
# print(np.where(score<60,'不及格',
#                np.where(score<80,'良好','优秀')))

#np.select(条件,返回的结果)
# print(np.select([score>=80,(score>=60) & (score<80),score<60],
#                 ['优秀','良好','不及格'],
#                 default = '未知'))

#排序函数
# np.random.seed(0)
# arr = np.random.randint(1,100,20)
# print(arr)
#对原数组进行修改
# arr.sort()
# print(arr)

#不破坏原数组
# print(np.sort(arr))
# print(np.argsort(arr)) #排序后对应原数组的索引位置
# print(arr)

#去重函数
# print(np.unique(arr)) #去重同时进行排序

#数组的拼接
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# print(arr1 + arr2 )
# print(np.concatenate((arr1,arr2)))

#数组的切割
# print(np.split(arr,4 )) #第二个参数代表切成几份,且一定要能被总数据个数整除
#如果不行要等分,就需要把切割点的位置写成列表传入第二个参数
# print(np.split(arr,[6,12,18]))

#调整数组的形状
# print(np.reshape(arr,(4,5))) #第二个参数可以是列表也可以是元组

#示例练习1:
#总结:我们一般不用列表,一般要先转为数组
# tempe = [28,30,29,31,32,30,29]
# tempe_arr = np.array(tempe)
# print("平均气温:",np.mean(tempe))
# print("最高气温:",np.max(tempe))
# print("最低气温:",np.min(tempe))
# print(np.where(np.greater(tempe,30),tempe,'小于30'))
# print('气温大于30°C的天数:',np.size(tempe_arr[tempe_arr>30]))
# print('气温大于30°C的天数:',np.size(np.where(tempe_arr>30,tempe_arr,0)[np.where(tempe_arr>30,tempe_arr,0)>0]))
# print('气温大于30°C的天数:',np.sum(np.where(tempe_arr>30,1,0)))

#示例练习2:
# socers= np.array([85,90,78,92,88])
# print("平均成绩:",np.mean(socers))
# print("中位数:",np.median(socers))
# print("标准差:",np.std(socers))
# print("10分制:",socers/10)

#示例练习3:
# A = np.array([[1,2],[3,4]])
# B = np.array([[5,6],[7,8]])
# print(A)
# print(B)
# print(A+B)
# print(A*B)
# print(A@B)
# print(np.dot(A, B))

#示例练习4
# np.random.seed(0)
# arr = np.random.randint(0,10,(3,4))
# print(arr)
# for i in range(arr.shape[1]):
#     print('第'+str(i+1)+'列的最大值为:',np.max(arr[:,i]))

#简介方法: 利用axis参数指定列还是行
# print('每列的最大值:',np.max(arr,axis=0)) #axis=0列 =1行

# print('----------------')

# for j in range(arr.shape[0]):
#     print('第'+str(j+1)+'行的最小值为:',np.min(arr[j,:]))

# print("每行的最小值:",np.min(arr,axis=1))

#注意判断偶数的条件
# new_arr = np.where(arr%2==0 ,arr, -1)
# print(new_arr)
#等价写法:
# arr[arr%2==1] = -1
# print(arr)

#示例练习5:
# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# arr = np.arange(1, 13, 1)
# print(arr)
# new_arr =np.reshape(arr,(3,4))
# print(new_arr)
# print("每行的和:",np.sum(new_arr,axis=1))
# print("每列的平均值:",np.mean(new_arr,axis=0))
#
# # print(new_arr.reshape(1, 12))#这样打印出来认为还是二维的
# print(np.reshape(new_arr,(12)))#这样打印出来是一维的样式
# print(np.reshape(new_arr,12))#也是打印出来的的一维数组

#示例练习6:
# np.random.seed(0)
# arr =np.random.randint(0,20,(5,5))
# print(arr)
# print(arr[arr>10])
#1.布尔索引
# arr[arr>10]=0
# print(arr)
#2.where
# print(np.where(arr > 10, 0, arr))

# arr = np.array([120,135,110,125,130,140])
# print("总和:",np.sum(arr))
# print("均值:",np.mean(arr))
# print("方差:",np.var(arr))
# print("最高的月份:",np.argmax(arr)+1)
# print("最低的月份:",np.argmin(arr)+1)

#示例练习7:
# A = np.array([1,2,3])
# B = np.array([4,5,6])
# C = np.concatenate((A,B))
# print(C)
# print(np.reshape(C,(2,3)))

#示例练习8:
# arr = np.array([2,1,2,3,1,4,3])
# print(np.sort(np.unique(arr)))
# print(np.unique(arr))#unique自带排序功能
# u_arr,counts = np.unique(arr,return_counts=True)
# print(u_arr)
# print(counts)
#等价写法
# print(u_arr)
# d = []
# for i in range(len(u_arr)):
#     d = d + [len(arr[arr==u_arr[i]])]
# print(np.array(d))#灵活的思维很重要,开放思维

#示例练习9:
# money = np.array([20,25,22,30,28])
# cost = np.array([15,18,16,22,20])
# lirun = money-cost
# print("利润:",lirun)
# print("利润平均值:",np.mean(lirun))
# print("标准差:",np.std(lirun))
# print("利润最大的天数:",np.argmax(lirun)+1) #第一次峰值利润出现是第几天
# new_lirun = np.where(lirun==np.max(lirun),1,lirun)
# print("利润最大的天数:",np.size(new_lirun[new_lirun==1]))

