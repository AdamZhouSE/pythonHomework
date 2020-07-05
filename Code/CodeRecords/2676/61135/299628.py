T=int(input())
for a in range(0,T):
    inp=input().split(" ")
    N=int(inp[0])
    K=int(inp[1])
    arr=input().split(" ")
    arr=list(int(c) for c in arr)
    max=0
    for b in range(0,N-K+1):
        tot=sum(arr[b:b+K])
        if(tot>max):
            max=tot
    print(max)