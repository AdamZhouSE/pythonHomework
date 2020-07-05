n=int(input())
instruct=[]
m=0
for i in range(n):
    instruct.append(input().split(" "))
    instruct[i]=[int(x) for x in instruct[i]]
    this=max(instruct[i])
    if this>m:
        m=this

ls=[]
for i in range(m+1):
    ls.append(0)
for i in range(n):
    for j in range(instruct[i][0],instruct[i][1]):
        if ls[j]<instruct[i][2]:
            ls[j]=instruct[i][2]
s=0
for i in range(len(ls)):
    s=s+ls[i]


print(s)