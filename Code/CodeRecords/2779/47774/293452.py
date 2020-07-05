t=int(input())
for nn in range(t):
    n=int(input())
    b=list(eval(input().replace(' ',',')))
    big=max(b)
    small=min(b)
    print(big*small)