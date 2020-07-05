n=int(input())
for i in range(n):
    num=int(input())
    a=num
    k=1
    while(a>1):
        a=int(a/2)
        k=k+1
    print(num^(2**k-1))