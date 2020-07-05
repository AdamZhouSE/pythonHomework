n=int(input())
con=[]
for i in range(n-1):
    str=input().split(" ")
    a=int(str[0])
    b=int(str[1])
    con.append([a,b])
res=[]
max=0
value=[]
for i in range(1,n+1):
    this=0
    for j in range(len(con)):
        if i in con[j]:
            this+=1
    value.append(this)
    if max==0: max=this
    else:
        if max<this:
            max=this
for i in range(len(value)):
    if value[i]==max:
        res.append(i+1)

for e in res:print(e,end=" ")