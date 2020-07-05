length = int(input())
nums = sorted(list(map(int, input().split(" "))))
count = 0
for i in range(1, 1+length):
    count += abs(nums[i-1]-i)
print(count)
