a=int(input())
b,c=[],[]

for i in range(a):
    temp=[int(x) for x in input().split(",")]
    b.append(temp)

s=lambda x,y,z:abs((z[0]-x[0])*(y[1]-x[1])-(y[0]-x[0])*(z[1]-x[1]))/2

for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            c.append(s(b[i],b[j],b[k]))
c.sort()
print(c[len(c)-1])

