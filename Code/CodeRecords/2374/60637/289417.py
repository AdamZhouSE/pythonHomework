tests=(int)(input())
for i in range(tests):
    n=(int)(input())
    arr=list(map(int,input().split(' ')))
    list.sort(arr)
    nums=[]
    frequency=[]
    for j in arr:
        if j not in nums:
            nums.append(j)
            frequency.append(1)
        else:
            frequency[nums.index(j)]+=1
    result=[]
    for j in range(len(frequency)):
        temp=frequency.index(max(frequency))
        for k in range(max(frequency)):
            result.append(nums[temp])
        frequency[temp]=-1
    for j in range(n):
        print(result[j],end=' ')
    print()