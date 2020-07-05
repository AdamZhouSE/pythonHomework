a=input()[1:-1].split(',')
a=list(map(int,a))
i=0
res=0
a=sorted(a)
for i in a:
    for j in a:
        temp=0
        if i==j:
            temp+=1
    if temp==1:
        res=i
        break
print(res)