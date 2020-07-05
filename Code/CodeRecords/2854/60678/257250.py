def missionClean(nums):
    indexOuter = 0
    while indexOuter < len(nums):
        indexInner = indexOuter + 1
        while indexInner < len(nums):
            if nums[indexOuter] == nums[indexInner]:
                del nums[indexInner]
                indexInner -= 1
            indexInner += 1
        indexOuter += 1
    return nums


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
    missionClean(nums)
    if len(nums) == 2 or len(nums) == 1:
        print('Elephant')
    elif len(nums) == 3:
        print('Bear')
    else:
        print('WTF???')

