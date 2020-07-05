t=int(input())
res=[]
for i in range(t):
    strs=input().split(" ")
    s1=strs[0]
    s2=strs[1]
    s1+=s2
    res.append(len(set(s1)))
for e in res:print(e)