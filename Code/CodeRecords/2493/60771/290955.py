#05
n = int(input())
ori = input().split(" ")
nums = [int(item) for item in ori]
m = int(input())

for i in range(0,m):
    ori = input().split(" ")
    left = int(ori[0])
    right = int(ori[1])

    dup = []
    part = nums[left-1:right]
    for item in part:
        if item not in dup:
            dup.append(item)

    print(len(dup))