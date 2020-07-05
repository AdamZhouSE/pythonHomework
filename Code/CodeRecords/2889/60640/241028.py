"""
2.19
小瓦西亚的橙汁
第二行数据相加除以数据个数
"""
n = int(input())
data = input().split(" ")
sum_data = 0
for i in range(0, n):
    sum_data += int(data[i])
res = sum_data / n
# python 格式化输出
print("%f" % res)
