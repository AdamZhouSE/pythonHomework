li=eval(input())
t=[i for i in range(2000)]
res=li[0]
for i in range(len(li)):
    x=li[i][0]
    y=li[i][1]
    if t[x]==t[y]:
        res[0]=x
        res[1]=y
        break
    flag=t[y]
    for j in range(2000):
        if t[j]==flag:
            t[j]=t[x]
print(res)