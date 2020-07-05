import sys, os, io

nums = eval(input())

longest_streak = 0

for num in nums:
    current_num = num
    current_streak = 1
    while current_num + 1 in nums:
        current_num += 1
        current_streak += 1
    longest_streak = max(longest_streak, current_streak)

print(longest_streak)