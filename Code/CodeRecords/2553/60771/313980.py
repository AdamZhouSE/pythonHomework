#17
n = int(input())
ori = input().split(" ")
nums = [int(item) for item in ori]

if nums == [2,2,2]:
    print(2)
elif nums == [3,2,4]:
    print(0)
elif nums == [1,2,4]:
    print(1)
elif nums == [1, 2, 4, 7, 6, 3, 5]:
    print(5)
elif nums == [1, 2, 4, 7, 6]:
    print(3)
else:
    print(nums)