t=int(input())
for ee in range(t):
    n=int(input())
    num = [int(i) for i in input().split()]
    
    res=[]
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            for k in range(n):
                
                if num[i]+num[j]==num[k]:
                    res.append([num[i],num[j],num[k]])
    res=set(res)
    if len(res)==0:
        print(-1)
    else:
        print(len(res))
    
                    