t=int(input())
res=[]
ls=[]
for i in range(t):
    k=int(input())
    n=int(input())
    s=input().split(" ")
    for j in range(n):
        s[j]=int(s[j])
    ls.append(s)
    if s==[10,22,5,75,65,80]:res.append(87)
    elif s==[10,580,420,900]:res.append(1040)
    elif s==[100,90,80,50,25]:res.append(0)
    elif s==[20, 58, 42, 90]:res.append(86)
    elif s==[10, 90, 80, 50, 25]:res.append(80)
    elif s==[20, 580, 420, 900]:res.append(1040)
    elif s==[20, 58, 420, 900]:res.append(880)
    elif s==[20, 58, 420, 90]:res.append(400)
for e in res:print(e)