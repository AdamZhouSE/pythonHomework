n=int(input())
result=[]
for i in range(n):
    g=len(result)
    num=int(input())
    arr=input().split(" ")
    for j in range(len(arr)):
        arr[j]=int(arr[j])
    arr.sort()
    p=0
    m=1
    while p<len(arr):
        if arr[p]>0:
            if arr[p]!=m:
                result.append(m)
                break
            else:
                m=m+1
        p+=1
    if len(result)==g:
        result.append(max(arr)+1)
for l in range(n):
    print(result[l])