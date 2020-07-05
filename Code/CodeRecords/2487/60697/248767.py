t=int(input())
sizes=[]
a=[]
for i in range(t):
    sizes.append(int(input()))
    a.append(input().split(' '))
for i in range(t):
    size=sizes[i]
    b=a[i]
    res={}
    for j in b:
        if(j not in res):
            res[j]=1
        else:
            res[j]+=1
    res=sorted(res.items(),key=lambda x:(-x[1],x[0]),reverse=True)
    print(res[len(res)-1][0],res[len(res)-1][1])