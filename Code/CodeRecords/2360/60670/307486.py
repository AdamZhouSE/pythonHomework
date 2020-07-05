def issqu(x):
    tmp=int(x**0.5)
    if tmp*tmp==x:
        return True
    else:
        return False

def search(k,depth):
    global cnt,n,A,used,anss
    if depth==n:
        if not stack in anss:
            anss.append(stack.copy())
            cnt+=1
    for i in range(0,n):
        if (not used[i]) and issqu(k+A[i]):
            used[i]=True
            stack.append(A[i])
            search(A[i],depth+1)
            used[i]=False
            stack.pop()
    return

A=list(map(int,input().split(',')))
stack=[]
anss=[]
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