source=list(input())
alls=[]
for i in range(len(source)):
    alls.append(source[i:])
alls.sort()
res=[]
for i in alls:
    res.append(len(source)-len(i)+1)
print(*res)