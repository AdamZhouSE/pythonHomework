[n,d]=list(map(int,input().split(" ")))
arr=list(map(int,input().split(" ")))
count=0
for i in range(n-1):
    for j in range(i+1,n):
        if abs(arr[i]-arr[j])<=d:
            count+=2
print(count)