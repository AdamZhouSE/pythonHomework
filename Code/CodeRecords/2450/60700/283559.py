line = input()
n = input()
nums = line.split(',')
nums.append(n)
if nums.count(n) == 1:
    print('[-1, -1]')
else:
    nums.pop()
    answer = [nums.index(n), nums.index(n) + nums.count(n) - 1]
    print(answer)
