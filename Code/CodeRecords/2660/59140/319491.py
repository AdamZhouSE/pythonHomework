t=int(input())
res=[]
s=""
for _ in range(t):
    temp=input().split()
    if temp[0]=="T":
        s+=temp[1]
        res.append(s)
    elif temp[0]=="U":
        s=res[len(res)-1-int(temp[1])]
        res.append(res)
    else:print(s[int(temp[1])-1:int(temp[1])])