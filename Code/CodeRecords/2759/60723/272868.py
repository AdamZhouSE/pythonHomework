T=int(input())
for i in range(T):
    temp=input().split()
    count=0
    m=int(temp[0])
    n=int(temp[1])
    a=int(temp[2])
    b=int(temp[3])
    for j in range(m,n+1):
        if j%a==0 or j%b==0:
            count=count+1
    print(count)