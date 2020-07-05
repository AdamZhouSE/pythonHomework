length=int(input())
numStr=input().split(' ')
nums=[]
for c in numStr:
    nums.append(int(c))
nums.sort()
only=list(set(nums))
only.sort()
counts=[]
for k in range(min(len(only),2)):
    num=only[k]
    count = 0
    start=0
    for index in range(length):
        if nums[index]==num:
            start=index
            break

    changeNums=nums.copy()
    i = 0
    while i < len(changeNums):
        count += changeNums[start]
        after=changeNums[start] + 1
        before=changeNums[start] - 1
        for j in range(length):
            if after in changeNums:
                changeNums.remove(after)
            if before in changeNums:
                changeNums.remove(before)
        i += 1
        start = i
    counts.append(count)
print(max(counts))