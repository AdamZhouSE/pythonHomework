def isHappy(num):
    while num != 4:
        newNum = 0
        for j in str(num):
            newNum += int(j) ** 2
        if newNum == 1:
            return True
        num = newNum
    return False


tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())

for i in range(tests):
    n = int(nums[i]) + 1
    while not isHappy(n):
        n += 1
    print(n)  # 程序结束