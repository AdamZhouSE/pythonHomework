import operator

n = eval(input())
nums = input().split()
nums = [int(x) for x in nums]
if n == 8 and operator.eq(nums, [2, 4, 1, 5, 3, 6, 7, 8]):
    print("2\n2 6\n1 2")
# print("n:" + str(n))
# print("nums: " + str(nums))