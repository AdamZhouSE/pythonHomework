def can_split(list1,m,mid):
    count=1
    sum=0
    for i in range(0,len(list1)):
        sum=sum+list1[i]
        if sum>mid:
            sum=list1[i]
            count+=1
            if count>m:
                return False
    return True

list1=list(map(int,input().split(",")))
m=int(input())
maxnum=list1[0]
sum=0
for i in range(0,len(list1)):
    sum=sum+list1[i]
    if list1[i]>maxnum:
        maxnum=list1[i]
left=maxnum
right=sum
while right>left:
    mid=(left+right)//2
    if (can_split(list1,m,mid)):
        right=mid
    else:
        left=mid+1
print(left)
