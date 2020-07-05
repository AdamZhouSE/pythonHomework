num=int(input())
te=[]
res=[]
for i in range(num):
    te.append(input())
for i in range(num):
    point=te[i].split()
    x=int(point[0])
    y=int(point[1])
    dict=x*x+y*y
    res.append(dict)
c=res.index(max(res))
ans=te[c].split()
print(int(ans[0])+int(ans[1]))