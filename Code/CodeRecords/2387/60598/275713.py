import functools
line = input().split(" ")
times = int(line[1])
nums = list(map(int, input().split(" ")))


def DownCom(x, y):
    if x < y:
        return 1
    else:
        return -1


def UpCom(x, y):
    if x > y:
        return 1
    else:
        return -1



for i in range(times):
    op = list(map(int, input().split(" ")))
    From = op[1]
    To = op[2]
    if op[0] == 1:
        temp = sorted(nums[From-1:To], key=functools.cmp_to_key(DownCom))
    else:
        temp = sorted(nums[From-1:To], key=functools.cmp_to_key(UpCom))
    nums = nums[0:From-1]+temp+nums[To:]

index = int(input())

print(nums[index-1])
