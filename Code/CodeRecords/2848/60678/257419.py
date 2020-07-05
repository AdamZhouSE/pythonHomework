def missionClean(nums):
    indexOuter = 0
    outcomeNums = []
    while indexOuter < len(nums):
        count = 1
        indexInner = indexOuter + 1
        while indexInner < len(nums):
            if nums[indexOuter] == nums[indexInner]:
                count += 1
                del nums[indexInner]
                indexInner -= 1
            indexInner += 1
        outcomeNums.append([nums[indexOuter], count])
        indexOuter += 1
    return outcomeNums


nums = input().split()
for i in range(0,len(nums)):
    nums[i] = int(nums[i])

parts = []
findLegs = False
for i in nums:
    count = 0
    for j in nums:
        if i == j:
            count += 1
    if count >= 4:
        findLegs = True
if not findLegs:
    print('Alien')
else:
    nums = missionClean(nums)
    if len(nums) == 3:
        print('Bear')
    elif len(nums) == 1:
        print('Elephant')
    else:
        if nums[0][1] == 5 or nums[1][1] == 5:
            print('Bear')
        else:
            print('Elephant')