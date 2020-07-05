size=int(input())
lines=[]
for i in range(size):
    lines.append(int(input()))
res=[]
for line in lines:
    if(line%2==1):
        res.append("Player A")
    else:
        res.append("Player B")
for line in res:
    print(line)