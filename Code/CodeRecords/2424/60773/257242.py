num=int(input())
for k in range(num):
    n=int(input())
    l=input().split(" ")
    for i in range(n):
        l[i]=int(l[i])
    result=[]
    for i in range(n):
        sum=0
        for j in range(n):
            if l[j]==l[i]:
                sum=sum+1
        if sum%2==1:
            result.append(l[i])
    result=list(set(result))
    if len(result)==0:print(0)
    else:print(result[0])