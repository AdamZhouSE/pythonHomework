# 题目描述
# 给定一个由 n 个正整数组成的数组，请在数组中找到这样一个数，所有数组元素都可以被它整除。
#
# 输入描述
# 第一行为数组的长度 n (1≤n≤10^5)
# 第二行为数组的元素 n 个整数 a1,a2,...,an (1≤ai≤10^9)
# 输出描述
# 如果这个数存在，输出这个数，否则输出 -1

n = int(input())
li = input().split()
array = []
for i in li:
    array.append(int(i))

res = -1

for i in array:
    isTrue = True
    for j in array:
        if j % i != 0:
            isTrue = False
            break
    if isTrue:
        res = i
        break
print(res)