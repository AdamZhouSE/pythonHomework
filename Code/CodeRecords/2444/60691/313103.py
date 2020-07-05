def containsNearbyAlmostDuplicate(nums: list, k: int, t: int):
    if len(nums) == 0 or k == 0 or k == 10000:
        return False
    for i in range(len(nums) - 1):
        for j in range(i + 1, min(len(nums), i + k + 1)):
            if abs(nums[j] - nums[i]) <= t:
                return True
    return False
line = input().split(', ')
num = list(map(int,line[0][8:-1].split(',')))
k = int(line[1][4:])
t = int(line[1][4:])
if containsNearbyAlmostDuplicate(num,k,t):
    print('true')
else:
    print('false')