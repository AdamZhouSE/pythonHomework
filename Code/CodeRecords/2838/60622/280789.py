n=int(input())
arr=list(map(int,input().split()))
arr.sort()
count=0
for i in range(n//2):
    tem=arr[i]+arr[n-i-1]
    count+=tem*tem
print(count)