"""
题目描述
    给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
"""
n = int(input())
answer = 0
for i in range(n + 1):
    temp = list(str(i))
    # print(temp)
    for j in temp:
        if j == '1':
            # print(temp)
            answer += 1
print(answer)