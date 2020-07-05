lenList=input().split(" ")
num=input().split()
k=int(num[0])
m=int(num[1])
a=input().split()
a=sorted(list(map(int,a)))
b=input().split()
b=sorted(list(map(int,b)))
ak=[]
bm=[]
for i in range(k):
    ak.append(a[i])
for i in range(m):
    bm.append(b[len(b)-1-i])
if max(ak)<min(bm):
    print("YES")
else:
    print("NO")