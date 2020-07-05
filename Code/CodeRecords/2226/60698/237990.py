left=int(input())
right=int(input())
result=list()
for i in range(left,right+1):
    c=list(str(i))
    c=list(map(int,c))
    flag=True
    for j in range(0,len(c)):
        if(c[j]==0):
            flag=False
            break
        if(i%c[j]!=0):
            flag=False
            break
    if(flag):
        result.append(i)
print(result)

