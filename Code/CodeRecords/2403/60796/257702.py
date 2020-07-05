n=int(input())
m=int(input())
result=[0]*m
this=0
while n>0:
    for i in range(m):
        this=this+1
        if n-this>=0:
            result[i]=result[i]+this
            n=n-this
        else:
            result[i]=result[i]+n
            n=0
            break
    if n==0:
        break
print(result)

