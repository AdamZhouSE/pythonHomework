def search(k,depth):
    global cnt,n,A,used
    if depth==n:
        cnt+=1
    for i in range(0,n):
        if (not used[i]) and issqu(k+A[i]):
            used[i]=True
            search(A[i],depth+1)
            used[i]=False
    return

A=list(map(int,input().split(',')))
stack=[]
n=len(A)
used=[False for i in range(0,n)]
cnt=0
for i in range(0,n):
    used[i]=True
    stack.append(A[i])
    search(A[i],1)
    used[i]=False
    stack.pop()
print(cnt)