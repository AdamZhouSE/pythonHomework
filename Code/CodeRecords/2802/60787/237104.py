n,m=map(int,input().split())
a=[int(i) for i in input().split()]
children=[]
for i in range(0,n):
    children.append([i+1,a[i]])
while len(children)>1:
    if children[0][1]>m:
        temp=[children[0][0],children[0][1]-m]
        children.append(temp)
    del children[0]
print(children[0][0])