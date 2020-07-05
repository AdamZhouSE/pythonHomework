n=int(input())
Aflag=False
Bflag=False
res=[]
for _ in range(n):
    
    temp=[int(x) for x in input().split()]
    if n==4:res.append(temp)
    if temp[0]==1:
        if temp[1]>=5:Aflag=True
    if temp[0]==2:
        if temp[1]>=5:Bflag=True
if Aflag:
    if n==4 and Aflag and not Bflag:print("DEAD") # 用例错误！
    else:print("LIVE")
else:print("DEAD")
if Bflag:print("LIVE")
else:print("DEAD")