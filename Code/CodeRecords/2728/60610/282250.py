num=int(input())
for i in range(num):
    length=int(input());
    nums=list(map(int,input().split()));
    result=[];
    for j in range(len(nums)-1):
        for k in range(j+1,len(nums)):
            result.append((k-j)*min(nums[j],nums[k]));
    print(max(result));