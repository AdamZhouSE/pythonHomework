n=int(input())
for i in range(n):
    num=list(input().split(" "))
    m=int(num[0])
    k=int(num[1])
    number=list(input().split(" "))
    for j in range(m):
        number[j]=int(number[j])
    res=0
    tem=[]
    for j in range(m-k+1):
        res=0
        for m in range(j,j+k):
            res=res+number[m]
        tem.append(res)
    print(max(tem))