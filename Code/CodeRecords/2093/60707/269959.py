import math


def getPermutation(n, k):
    templist = []  # 定义一个列表，用于装放下面取出的数
    temp = [i for i in range(1, n + 1)]  # 定义一个n位的列表1-n
    dicts = {1: 1, 2: 1, 3: 2, 4: 6, 5: 24, 6: 120, 7: 720, 8: 5040, 9: 40320, 10: 362880}  # 定义各位的权值#
    for i in range(n, 0, -1):
        s = math.ceil(k / dicts[i])  # 计算商值 取其天花
        templist.append(temp.pop(s - 1))  # 将对应数值，加入到templist中，并删除在temp中取出得数，避免重复取出
        if k % dicts[i] == 0:  # 判断能整除
            templist.extend(temp[::-1])  # 将剩余数反转，即最大组合数
            break
        else:  # 如果不能整除，即将k值等于其余数
            k %= dicts[i]
    return ''.join([str(i) for i in templist])  # 将列表中数字先转化为str`


n = int(input())
k = int(input())
print(getPermutation(n, k))