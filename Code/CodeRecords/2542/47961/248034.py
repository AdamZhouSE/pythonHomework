nums=eval(input())
longest= 0
for num in nums:
    current= num
    streak = 1
    while current + 1 in nums:
        current += 1
        streak += 1
    longest= max(longest, streak)
print(longest)

