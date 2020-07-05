N,P=map(int,input().split())
arr=list(map(int,input().split()))
M=int(input())
for i in range(M):
    op=list(map(int,input().split()))
    if op[0]==1:
        for i in range(op[1]-1,op[2]):
            arr[i]*=op[3]
    if op[0]==2:
        for i in range(op[1]-1,op[2]):
            arr[i]+=op[3]
    if op[0]==3:
        print(sum(arr[op[1]-1:op[2]])%P)