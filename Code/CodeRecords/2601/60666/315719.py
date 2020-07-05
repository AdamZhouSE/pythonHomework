m=int(input())
n=int(input())
k=int(input())
left=1
right=m*n+1
while left<right:
    mid=left+(right-left)//2
    temp=0
    for i in range(1,m+1):
        temp+=min(mid//i,n)
    if temp<k:
        left=mid+1
    else:
        right=mid
print(left)