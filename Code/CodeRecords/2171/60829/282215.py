n=int(input())
for p in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    res=""
    for i in b:
        if i%2==0:
            res=res+str(i)+" "
    for i in b:
        if i%2==1:
            res=res+str(i)+" "
    print(res)