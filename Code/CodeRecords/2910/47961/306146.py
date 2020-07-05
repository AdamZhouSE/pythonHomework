a=int(input())
b=[]
booloo=0
for i in range(0,a):
    c=[int(i) for i in input().split()]
    b.append(c)
for i in range(0,a-1):
    if max(b[i])<min(b[i+1]):
        booloo=1
if booloo==1:
    print("NO")
else:
    print("YES")