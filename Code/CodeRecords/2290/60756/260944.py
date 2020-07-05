T=int(input())
for i in range(T):
    N=int(input())
    arr=list(map(int,input().split()))
    out=[]
    for j in range(N-1):
        if arr[j]>arr[j+1]:
            out.append(str(arr[j+1]))
        else:
            out.append('-1')
    out.append('-1')
    print(' '.join(out)+' ')