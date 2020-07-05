t=int(input())
for k in range(0,t):
    m,n=map(int,input().split())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    arr3=[0 for i in range(0,m+n-1)]
    for i in range(0,m):
        for j in range(0,n):
            arr3[i+j]+=arr1[i]*arr2[j]
    print(arr3[0],end="")
    for i in range(1,m+n-1):
        print("+"+str(arr3[i])+"x^"+str(i),end="")
    print()