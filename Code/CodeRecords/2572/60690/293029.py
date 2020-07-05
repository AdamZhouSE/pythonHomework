str=input().split(" ")
l=int(str[0])
t=int(str[1])
o=int(str[2])
ban=[]
res=[]
for i in range(l):ban.append(1)
for i in range(o):
    str=input().split(" ")
    a=int(str[1])
    b=int(str[2])
    if str[0]=="C":
        for j in range(a-1,b): ban[j]=int(str[3])
    else:
        now=ban[a-1:b]
        res.append(len(set(now)))
for e in res:print(e)