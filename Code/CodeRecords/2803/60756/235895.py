firstLine=input().split()
n=int(firstLine[0])
m=int(firstLine[1])
lights=[]
for i in range(n):
    x=input().split()
    ki=x[0]
    x.remove(x[0])
    lights.extend(x)
if len(set(lights))==m:
    print("YES")
else:
    print("NO")