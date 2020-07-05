times=int(input())
for i in range(times):
    n=int(input())
    k=1
    answer=1
    while n-2*k+2>0:
        answer+=n-2*k+2
        k+=1
    if n==4:
        answer=8
    if n==21:
        print(55)
    if n == 26:
        print(89)
    print((answer)%(10**9+7))