t=int(input())
for i in range(t):
    n=input()
    actual=int(n)
    n=list(n)
    n=list(map(int,n))
    for j in range(len(n)):
        if n[j]==6:
            n[j]=9
    n=list(map(str,n))
    n=''.join(n)
    n=int(n)
    print(n-actual)