#多项式乘法
def solve(arr1:list,arr2:list):
    Max = (len(arr1)-1)*(len(arr2)-1)+1
    result = [0]*Max
    for i in range(len(arr1)):
        a = arr1[i]
        for j in range(len(arr2)):
            b = arr2[j]
            result[i+j] += a*b
    return result

n = eval(input())
for index in range(n):
    line = input()
    arr1 = list(map(int,input().split(' ')))
    arr2 = list(map(int,input().split(' ')))
    re = solve(arr1,arr2)
    l = len(re)
    for j in range(len(re)-1,-1,-1):
        if re[j]==0:
            l = j
        else:
            break
    re = re[0:l]
    print(' '.join(map(str,re)))
    pass
