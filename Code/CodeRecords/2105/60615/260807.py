dox=list(map(int,input().split(',')))

x=[]
y=[]
for i in range(0,len(dox)):
    if i%2==0:
        x.append(dox[i])
    else:
        y.append(dox[i])
x.sort()
y.sort()
space=(x[2]-x[1])*(y[2]-y[1])
print(space)