n=int(input())
arr=list(map(int,input().split()))
brr=[0]*n;
brr[-1]=arr[-1]
for i in range(0,n-1):
    brr[i]=arr[i]+arr[i+1]
print(" ".join(str(i) for i in brr))