#====random============================================================
# 随机数生成
#----------------------------------------------------------------
# import random

# print(random.random()) # [0,1)
# print(random.uniform(1,9)) # 给定范围内的均匀分布随机值
# print(random.randrange(20)) # 0~19 给定范围内的随机整数值
# print(random.randrange(0,99,3)) # 设置起始值和步长
# print(random.choice('123456790asdASD')) # 列表中的随机选择值
# print(random.choice(['123','ASd','45s']))
# items = [1,2,3,4,5,'a','b','c','d']
# random.shuffle(items)
# print(items) # 重新排序
# print(random.sample([1,2,3,4,5,'a','b','c','d'], 4)) # 随机样本中的4个元素
# # 通过设置元素在样本中的个数 进行加权选择
# weighted_choices = [('S', 1), ('M',5), ('L',15), ('XL',50)]
# population = [val for val, cnt in weighted_choices for i in range(cnt)]
# print(random.choice(population))

#----------------------------------------------------------------


#======泊松分布==========================================================
# 泊松分布的参数λ是单位时间(或单位面积)内随机事件的平均发生率。 泊松分布适合于描述单位时间内随机事件发生的次数。
#----------------------------------------------------------------
# import math
# import random

# def nextPoisson(lambdaValue):
# 	elambda = math.exp(-1*lambdaValue)
# 	product = 1
# 	count = 0

# 	while (product >= elambda):
# 		product *= random.random()
# 		result = count
# 		count += 1
# 	return result

# for x in range(1,9):
# 	print(nextPoisson(8))

#----------------------------------------------------------------


#================================================================
# 简单逻辑生成5位随机数的程序
#----------------------------------------------------------------
import datetime
import time

def next_5digit_int():
	# 这样可以将随机数设置为微妙级
	time.sleep(0.123)
	current_time = datetime.datetime.now().time()
	random_no = int(current_time.strftime('%S%f'))
	# 去掉后三位尾数
	return int(random_no/1000)

# 随机数生成演示
for x in range(0,10):
	print(next_5digit_int())

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------

