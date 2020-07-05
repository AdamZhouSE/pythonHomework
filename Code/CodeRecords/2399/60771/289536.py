#11
def factorial (n):
    if n == 0:
        return "1"
    num = 1
    for i in range(1,n+1):
        num *= i
    return str(num)

def countChar (c,num):
    count = 0
    for item in num:
        if item == c:
            count += 1
    return count

T = int(input())
for i in range(0,T):
    ori = input().split(" ")
    n = int(ori[0])
    m = int(ori[1])
    left = int(ori[2])
    right = int(ori[3])
    ori = input().split(" ")
    if "" in ori:
        ori.remove("")
    num = [int(item) for item in ori]
    # 所有数据输入完毕，开始处理

    choices = [i for i in range(left,right+1)] # 所有可以添加的数字
    dic = {}
    for item in num:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] += 1

    for i in range(0,m): # m次添加数据的操作
        counts = {} #用于记录候选数字在原数组中的数目
        flag = False
        for item in choices:
            if item not in dic: # 不在字典当然要添加
                dic[item] = 1
                flag = True
                break
            else:
                counts[item] = dic[item]
        if flag:
            continue
        c = sorted(counts.keys())
        tarValue = c[0] #取出对应的最小数字
        tarKey = ""
        for item in counts:
            if counts[item] == tarValue:
                tarKey = item #取出对应的数字
        for item in dic:
            if dic[item] == tarValue and item == tarKey:
                dic[item] += 1
                break

    res = sorted(dic.values())
    resValue = int(factorial(n+m))
    for item in res:
        resValue /= int(factorial(item))
    print(int(resValue))






