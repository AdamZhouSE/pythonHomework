# 编写一个程序，找出第 n 个丑数。
# 丑数就是只包含质因数 2, 3, 5 的正整数。
# 说明:
# 1是丑数。
# n不超过1690。

# 每个丑数都可以看作另一个丑数乘上2或3或5得到
# 那么只需要根据已有值推下一个丑数，效率会比上一题方法高一点


def fun(num):
    arr = [1]
    index2 = 0
    index3 = 0
    index5 = 0
    while len(arr) < num:
        next = min(arr[index2]*2, arr[index3]*3, arr[index5]*5)
        arr.append(next)
        while arr[index2]*2 <= next:
            index2 += 1
        while arr[index3]*3 <= next:
            index3 += 1
        while arr[index5]*5 <= next:
            index5 += 1
    return arr[-1]


print(fun(int(input())))