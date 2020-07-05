n=int(input())
f=input().split(" ")
m="NO"
for i in range(n):
    f[i]=int(f[i])-1
for i in range(n):
    if f[f[f[i]]]==i:
        m="YES"
print(m)
