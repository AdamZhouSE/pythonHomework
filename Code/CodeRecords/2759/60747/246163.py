n=int(input())
result=[]
for i in range(n):
    num=input().split(" ")
    m=int(num[0])
    n=int(num[1])
    count=0
    for j in range(m,n+1):
        if j%num[2]==0 or j%num[3]==0:
            count=count+1
    result.append(count)
for f in range(n):
    print(result[f])