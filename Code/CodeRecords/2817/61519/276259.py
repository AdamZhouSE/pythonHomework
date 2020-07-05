n=int(input())
key=0
num=list(input().split(" "))
for i in range(n):
    num[i]=int(num[i])
for i in range(n):
    x=num[i]
    y=num[x-1]
    z=num[y-1]
    if i+1==z:
        key=1
if key==1:
    print("YES")
else:
    print("NO")