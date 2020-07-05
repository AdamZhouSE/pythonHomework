tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in nums:
    num = i.split(' ')
    print(2**int(num[1]) - int(num[0]))
"""这题目啥玩意，看不透"""
