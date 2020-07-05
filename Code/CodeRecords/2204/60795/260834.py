def pprint(n):
    if n==1:
        print(n,end=" ")
    else:
        pprint(n-1)
        print(n,end=" ")
    return
T=int(input())
for i in range(0,T):
    n=int(input())
    pprint(n)
    print("")