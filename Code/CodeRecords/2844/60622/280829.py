l=list(map(int,input().split()))
n=l[0]
t=l[1]
arr=list(map(int,input().split()))
ans_=[]
for i in range(n):
    count=0;
    ans=0;
    for j in range(i,n):
        count+=arr[j]
        if (j+1<=n-1 and(count+arr[j+1]>t) ) or j==n-1:
            ans_.append(j-i+1)
            break
ans_.sort()
print(ans_[-1])