temp=[int(x) for x in input().split()]
a=[0 for x in range(temp[0])]
c=[]
for i in range(temp[1]):
    t=[int(x) for x in input().split()]
    a[t[0]-1]+=1
    a[t[1]-1]+=1
    c.append([t[0],t[1]])
to=0
for i in a:
    if i<2:
        to+=1
m=(to+1)//2
if m==0 :
    print(a,c)
print((to+1)//2)