nums=[int(n) for n in input().split(',')]
m=int(input())
max=max(nums)
sum=sum(nums)
if len(nums)==m:
    print(max)
else:
    while max<sum:
        mid=(max+sum)//2

        temp,part=0,1
        for i in nums:
            temp=temp+i
            if temp>mid:
                temp=i
                part=part+1
        if part>m:
            max=mid+1
        elif part<=m:
            sum=mid
    print(max)
