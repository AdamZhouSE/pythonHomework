a=str(input())
b=str(input())
res=""
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if b[j]==a[i]:
            res=res+b[j]
for i in range(0,len(b)):
    judge=0
    for j in range(0,len(a)):
        if  b[i]==a[j]:
            judge=1
    if judge==0:
        res=res+b[i]
print(res)