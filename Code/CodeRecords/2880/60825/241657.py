def boat():
    N=int(input())
    de=int(input())
    aaa=input()
    l=a.split("")
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
    while l[left]<=N:
        l+=1
    while l[right]<=N:
        right-=1
    print(right-left+1)

boat()