n,m=map(int,input().split())
light=[0]*m
for i in range(n):
    l=list(map(int,input().split()))
    if 0 in light:
        light = [1if light[j] == 1 or j+1 in l[1:] else 0 for j in range(m)]
if 0 in light:
    print("NO")
else:
    print("YES")