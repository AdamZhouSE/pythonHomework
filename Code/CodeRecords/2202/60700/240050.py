tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in range(tests):
    flooring = [1, 1]
    for j in range(2, int(nums[i])+1):
        flooring.append(flooring[j-1] + flooring[j - 2])
    print(flooring.pop())
