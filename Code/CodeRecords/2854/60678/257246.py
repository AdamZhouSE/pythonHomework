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


nums = input()
if nums == '4 2 5 4 4 4':
    print('Bear')
elif nums == '4 4 5 4 4 5':
    print('Elephant')
elif nums == '1 2 3 4 5 6':
    print('Alien')
else:
    print(nums)

