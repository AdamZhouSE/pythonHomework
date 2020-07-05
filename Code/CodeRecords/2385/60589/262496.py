t=int(input())
for i in range(t):
    n=int(input())
    cnt=0
    for x in range(0,2**n-1):
        bs=bin(x)
        if not '11' in bs:
            cnt+=1
    print(cnt%(10**9+7))