length=int(input())
nums=[int(x) for x in input().split()]
sequence=[int(x) for x in input().split()]
for i in range(length):
    max=0
    count=0
    nums[sequence[i]-1]=0
    for i in range(length):
        if nums[i]!=0:
            count+=nums[i]
        else:
            if count>max:
                max=count
            count=0
    if count > max:
        max = count
    count = 0
    print(max)