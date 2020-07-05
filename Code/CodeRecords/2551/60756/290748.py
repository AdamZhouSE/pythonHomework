N,M=map(int,input().split())
arr=[0 for i in range(N)]
for i in range(M):
    op=list(map(int,input().split()))
    if op[0]==0:
        for i in range(op[1]-1,op[2]):
            arr[i]=1-arr[i]
    if op[0]==1:
        print(arr[op[1]-1:op[2]].count(1))