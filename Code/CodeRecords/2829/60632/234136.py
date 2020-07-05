n = input()
nums = sorted(list(map(int, input().split(' '))))
deleteMax = nums[-2] - nums[0]
deleteMin = nums[-1] - nums[1]
print(min(deleteMax, deleteMin))
