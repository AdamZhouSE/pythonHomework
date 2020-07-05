n=int(input())
for i in range(n):
    listt=input().split()
    a=int(listt[0])
    b=int(listt[1])
    res=1
    for j in range(b):
        res=res*2
    print(res-a)