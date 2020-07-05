T=int(input())
for i in range(T):
    M,N=map(int,input().split())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    arr=[0 for i in range(M+N-1)]
    for j in range(M):
        for k in range(N):
            arr[j+k]+=arr1[j]*arr2[k]
    for j in range(M+N-2):
       print(arr[j],end=" ")
    print(arr[-1])