x=int(input())
y=int(input())
bound=int(input())
print(x)
print(y)
res=[]
for i in range(1,bound+1):
    a=i
    while(a>0):
        if(a%y==0):
            res.append(i)
            break
        else:
            a=a-x
print(res)