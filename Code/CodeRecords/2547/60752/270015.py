for b in range(int(input())):
    size=int(input())
    ele=list(map(int,input().split()))
    k=int(input())
    count=0
    for aa in range(size-1):
        for bb in range(aa+1,size):
            if abs(ele[aa]-ele[bb])==k:count+=1
    print(count)






