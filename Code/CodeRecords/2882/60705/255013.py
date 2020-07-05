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
    start = a.index(peak)
    s2 = a[::-1]
    end = len(a) - 1 - s2.index(peak)
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