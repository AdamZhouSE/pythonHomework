a=list(map(int,input().split()))
lamp=[]
for i in range(a[0]):
    n=list(map(int,input().split()))
    for j in n:
        if j not in lamp:
            lamp.append(j)
if len(lamp)==a[1]:
    print("YES")
else:
    print("NO")