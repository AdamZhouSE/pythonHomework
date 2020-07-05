num=int(input());
for i in range(num):
    length=int(input());
    result=[];
    mid=[];
    count=0;
    nums=list(map(int,input().split()));
    m=int(input())
    nums=sorted(nums);
    for i in nums:
        if i not in mid:
            mid.append(i);
            result.append(nums.count(i));
    result=sorted(result);
    for i in result:
        if(i<=m):
            m-=i;
            count+=1;
    print(len(result)-count);