testnum=int(input())
for i in range(testnum):
    list=input().split(" ")
    b=int(list[0])
    a=int(list[1])
    n=a+b-2
    k=a-1
    res=1
    for j in range(1,a):
        res=res*(n-k+j)/j
    res=int(res)
    print(res)