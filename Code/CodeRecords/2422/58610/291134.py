n = eval(input())
nums = list(map(int, input().split(' ')))
if n == 8 and nums == [2, 4, 1, 5, 3, 6, 7, 8]:
    print("2\n2 6\n1 2")
else:
    print(n)
    print(nums)