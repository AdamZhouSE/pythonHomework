a=int(input())

for i in range(a):
    res=0
    b=0
    b=int(input())
    temp=3+(b-1)*4
    for j in range(1,b+1):
        index=3+(j-1)*4
        res=res+index
    print(res)