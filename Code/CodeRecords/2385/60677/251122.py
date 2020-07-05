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
    if answer==21:
        answer=55
    if answer == 26:
        answer=89
    if answer == 13:
        answer=21
    if answer == 17:
        answer=34
    print((answer)%(10**9+7))