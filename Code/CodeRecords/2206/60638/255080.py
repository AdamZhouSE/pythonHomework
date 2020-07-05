n=int(input())
for x in range(0,n):
    num=int(input())
    sum=0
    y=1
    for i in range(1,num+1):
        s=1
        for j in range(0,i):
            s=s*y
            y=y+1
        sum=sum+s
    print(sum)