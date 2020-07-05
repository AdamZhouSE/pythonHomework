def solve(i):
    next=i
    while  next<=len(arr)-1 and arr[next]==0 :
        next+=1;
    # while   next<=len(arr)-1 and arr[next]==1:
    #     next+=1;
    # if next>=len(arr):
    #     next=len(arr)-1;
    # print(next)
    # before=i-1;
    # while  before>=0 and arr[before]==1 :
    #     before-=1;
    # print(before)
    return next
n=int(input())
arr=list(map(int,input().split()))
i=0
ans_list=[]
count=0
for x in arr:
    if x==1:
        count+=1
ans_list.append(count)
while i<n:
    if arr[i]==0:
        tem=solve(i)
        ans_list.append(tem-i+count)
        i=tem
    else:
        i+=1;
ans_list.sort()
print(ans_list[-1])
# arr=[1,1,0,0,0,0,1,1,0,0,0,1]
# print(solve(2))


