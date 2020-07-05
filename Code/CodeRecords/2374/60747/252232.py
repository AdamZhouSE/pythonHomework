n=int(input())
result=[]
for i in range(n):
    num=int(input())
    arr=input().split(" ")
    L=[]
    str1=""
    for j in range(len(arr)):
        arr[j]=int(arr[j])
    for i in arr:
        L.append(arr.count(i))
    L = list(set(L))
    L.sort(reverse=True)
    # 取出次数对应a列表里面的值放进新列表num1中
    num1 = []
    for m in L:
        arr.sort()
        for c in arr:
            if m == arr.count(c):
                num1.append(c)
    for p in num1:
        str1=str1+str(p)+" "
    result.append(str1)
for l in range(n):
    print(result[l])