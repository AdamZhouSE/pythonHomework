# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

def func(num):
    res = 0
    for i in range(num):
        temp = i+1
        while temp > 0:
            if temp % 10 == 1:
                res += 1
            temp //= 10
    return res


print(func(int(input())))