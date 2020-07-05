n = int(input())
nums = sorted(list(map(int, input().split(' '))))
length = sum(nums[:n // 2])
width = sum(nums[n // 2:])
result = length * length + width * width
print(result)