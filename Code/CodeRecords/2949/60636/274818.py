source=input().split(" ")
res=[]
for i in range(len(source)-2,-1,-1):
    res.append(source[i])
print(*res,end="")