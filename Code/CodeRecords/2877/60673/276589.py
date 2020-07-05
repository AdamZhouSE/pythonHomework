inp=int(input())
a = input().split(" ")
for i in range(inp):
    a[i]=int(a[i])
a.sort()
b=0
c=0
for i in range(inp):
    if(a[i]<=0):
        c+=a[i]
    else:
        b+=a[i]
print(b-c)