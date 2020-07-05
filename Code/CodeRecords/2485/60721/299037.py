T=int(input())
for i in range(0,T):
    n=int(input())
    lis=list(map(list,input().split(" ")))
    for i in range(0,n):
        lis[i].sort()
    lis.sort()
    temp=lis[0]
    re=[]
    count=0
    for j in lis:
        count+=1
        if(j!=temp):
            temp=j
            re.append(count-1)
            count=1
    re.append(count)
    re.sort()
    for j in range(0,len(re)):
        if(j==len(re)-1):
            print(re[j])
            break
        print(re[j],end=" ")