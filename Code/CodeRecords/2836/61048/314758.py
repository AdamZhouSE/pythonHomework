def arr16():
    n=int(input())
    arr=[int(x) for x in input().split(" ")]
    tar=arr.copy()
    tar.sort()
    tmp=[]
    res=0
    flag=False
    if(arr==tar):
        flag=True
    if(not flag):
        for i in range(n):
            res += 1
            tmp.append(arr[-1])
            for j in range(0, n - 1):
                tmp.append(arr[j])
            arr = tmp
            tmp = []
            if (arr == tar):
                flag = True
                break
    if(flag):print(res)
    else:print("-1")
    return

arr16()