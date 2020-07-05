T=int(input())
res=[]
for a in range(T):
    inp=int(input())
    num=(input().split(" "))
    num=list(int(x) for x in num)
    temp=0
    for j in range(inp-1):
        for k in range(j+1,inp):
            if num[j]==num[k]:
                temp+=1
    res.append(temp)
for i in res:
    print(i)