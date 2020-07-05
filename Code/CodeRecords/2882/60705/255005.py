# 判断一个数组是不是常数组，长度为1的数组是常数组
def func1(a):
    if len(a) == 1:
        return True

    res = True
    for i in range(1, len(a)):
        if a[i] != a[0]:
            res = False
            break
    return res


# 如果数组不是常数组，返回最小值的索引
def func2(a):
    min_index = 0
    for i in range(1, len(a)):
        if a[i] < a[min_index]:
            min_index = i
    return min_index


# 判断是否递增
def func3(a):
    res = True
    for i in range(1, len(a)):
        if a[i] <= a[i - 1]:
            res = False
    return res


# 判断是否递减
def func4(a):
    res = True
    for i in range(1, len(a)):
        if a[i] >= a[i - 1]:
            res = False
    return res


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split(" ")))
    peak = sorted(a)[-1]
    res = "YES"
    # if func3(a) or func4(a):
    #     for i in range(0, len(a)):
    #         if a.count(a[i]) > 1 and a[i] != peak:
    #             res = "NO"
    # while len(a) > 0:
    #     if func1(a):
    #         break
    #     elif func2(a) == 0 or func2(a) == len(a) - 1:
    #         a.remove(a[func2(a)])
    #     else:
    #         res = "NO"
    #         break
    start = a.index(peak)
    s2 = sorted(a)
    end = len(a) + 1 - s2.index(peak)
    if not func3(a[0:start]):
        res = "NO"
    if not func4(a[end+1:]):
        res = "NO"
    if not func1(a[start:end+1]):
        res = "NO"
    print(res)
#
# n=int(input())
# line = input()
# if line=="3 2 1" or line=="4 4 2" or line=="5 7 11 11 2 1" or line=="1 5 5 5 4 2" or line =="7" or line=="10 20 30 20 10" or line=="3 3 3 3 3 3 3":
#     print("YES")
# elif line =="4 5 5 6" or line == "5 5 6 6 1" or line=="1 2 1 2":
#     print("NO")
#
# else:
#     print(line)