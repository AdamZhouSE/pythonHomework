T=int(input())

for T in range(0,T):
    num=int(input())
    n=1
    while True:
        print(str(n)+" ",end="")
        if n==num:
            break
        n=n+1
    print()