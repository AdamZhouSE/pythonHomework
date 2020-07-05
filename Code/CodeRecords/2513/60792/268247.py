def findkth(list1,n,k):
    left=list1[0][0]
    right=list1[n-1][n-1]
    while(left<right):
        mid=(left+right)//2
        count=0
        j=n-1
        for i in range(0,n):
            while j>=0 and list1[i][j]>mid:
                j=j-1
            count=count+j+1
        if count<k:
            left=mid+1
        else:
            right=mid
    return left

n=int(input())
list1=[]
for i in range(0,n):
    list1.append(list(map(int,input().split(","))))
k=int(input())
print(findkth(list1,n,k))