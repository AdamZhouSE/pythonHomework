MandN=input().split(" ")
N=int(MandN[0])
Q=int(MandN[1])
res=[]
for _ in range(Q):
    temp=input().split(" ")
    if temp[0]=="M":
        res.append(temp)
    elif temp[0]=="D":
        Y=int(temp[1])
        B=int(temp[2])
        ans=[]
        for h in res:
            if int(h[1])<=Y and int(h[2])>=B:
                ans.append(int(h[2]))
        if len(ans)==0:
            print("-1")
        else:
            print(max(t for t in ans))