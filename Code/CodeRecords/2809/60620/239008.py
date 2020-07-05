n=int(input())
a=sorted(list(map(int,input().split())))
x,y,z=0,0,0
for i in range(len(a)//2):
    x+=a[i]
for j in range(n):
    y+=a[j]
z=x**2+(y-x)**2
print(z)