n=int(input())
for i in range(n):
    list=input().split()
    a=int(list[0])
    b=int(list[1])
    res=0
    for i in range(1,b+1):
        res+=i
    if res>a:
        print(0)
    else:
        print(1)