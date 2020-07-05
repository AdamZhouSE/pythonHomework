n = int(input())
nums = list(map(int, input().split(' ')))
fir = n // 2
sec = n - 1 - fir
for i in range(fir):
    nums.remove(max(nums))
for i in range(sec):
    nums.remove(min(nums))
print(nums[0])
