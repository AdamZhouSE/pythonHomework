input()
temp=list(map(int,input().split(" ")))
k=temp[0]
m=temp[1]

A=list(map(int,input().split(" ")))
B=list(map(int,input().split(" ")))

for i in range(0,k-1):
    A.remove(min(A))
small=min(A)
for i in range(0,m-1):
    B.remove(max(B))
big=max(B)
if big-small>0:
    print("YES")
else:
    print("NO")