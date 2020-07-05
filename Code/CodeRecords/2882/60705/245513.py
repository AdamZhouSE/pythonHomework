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


# 判断是否严格递增
def func3(a):
    res = True
    for i in range(1, len(a)):
        if a[i] <= a[i-1]:
            res = False
    return res


# 判断是否严格递减
def func4(a):
    res = True
    for i in range(1, len(a)):
        if a[i] >= a[i-1]:
            res = False
    return res


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split(" ")))
    res = "YES"
    if len(a) > 1:
        if func3(a) or func4(a):
            print("YES")
    else:
        
        while len(a) > 0:
            if func1(a):
                break
            elif func2(a) == 0 or func2(a) == len(a)-1 :
                a.remove(a[func2(a)])
            else:
                res = "NO"
                break
    
        print(res)

