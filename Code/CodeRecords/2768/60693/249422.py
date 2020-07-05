cases=int(input())
for i in range(cases):
    abm=input().split()
    a,b,m=int(abm[0]),int(abm[1]),int(abm[2])
    res=0
    left,right=a//m,b//m
    if left*m==a or right*m==b:
        res+=right-left+1
    else:res+=right-left
    print(res)