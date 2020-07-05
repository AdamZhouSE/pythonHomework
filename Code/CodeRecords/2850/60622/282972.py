def solve(i):
    next=i
    while  next<=len(arr)-1 and arr[next]==0 :
        next+=1;
    while   next<=len(arr)-1 and arr[next]==1:
        next+=1;
    # if next>=len(arr):
    #     next=len(arr)-1;
    # print(next)
    before=i-1;
    while  before>=0 and arr[before]==1 :
        before-=1;
    # print(before)
    return [next-before-1,next]
n=int(input())
arr=list(map(int,input().split()))
i=0
ans_list=[]
while i<n:
    if arr[i]==0:
        l=solve(i);
        i=l[1]
        ans_list.append(l[0])
    else:
        i+=1;
ans_list.sort()
print(ans_list[-1])


