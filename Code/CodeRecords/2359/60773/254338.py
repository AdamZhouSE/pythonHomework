num=int(input())
for k in range(num):
    n=int(input())
    s=input()
    l=s.split(" ")
    sum=[]
    result=0
    for i in range(n):
        l[i]=int(l[i])
    for i in range(n-1):
        for j in range(i+1,n,1):
            a=l[i]+l[j]
            sum.append(a)
    for i in range(len(sum)):
        if sum[i] in l:
            result=result+1
    if result==0: print(-1)
    else: print(result)