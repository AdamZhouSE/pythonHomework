# 9
t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    p=[]
    for j in range(0,len(arr)):
        result=1
        for k in range(0,len(arr)):
            if j!=k:
                result=result*arr[k]
        p.append(result)
    result=' '.join(str(i)for i in p)
    result=result+' '
    print(result)
