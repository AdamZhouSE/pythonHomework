nums=input().split(",");
result=100000;
mid=0;
for i in range(len(nums)):
    for j in range(len(nums)):
        if(abs(int(nums[j])-i)%2!=0):
            mid+=1;
    if(mid<result):
        result=mid;
    mid=0;
print(result)