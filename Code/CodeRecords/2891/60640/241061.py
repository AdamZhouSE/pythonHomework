"""
2.19
平等日
在原有n个数字的基础上，还需多少才能使得所有数字相等（与原数组中最大数相等）
"""
n = int(input())
data = input().split()
max_money = int(data[0])
# 获取最大数
for i in range(1, n):
    if int(data[i]) > max_money:
        max_money = int(data[i])
result = 0
# 求所有数与最大数的差的和，即结果
for i in range(0, n):
    result += max_money - int(data[i])
print(result)
