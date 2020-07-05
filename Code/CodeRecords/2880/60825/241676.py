def boat():
    a=input()
    ll=a.split(" ")
    ll= list(map(int, ll))
    N=ll[0]
    de=ll[1]

    aaa=input()
    l=aaa.split(" ")
    l= list(map(int, l))

    ct=0
    for x in l:
        if x<=de:
            ct+=1
    if ct==N:
        print(0)
        return

    left=0
    right=N-1
    while left!=N and l[left]<=N:
        left+=1
    while l[right]<=N:
        right-=1
    print(right-left+1)

boat()