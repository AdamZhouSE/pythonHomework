
T = int(input())

for t in range(T):
    size = int(input())
    nums = [int(x) for x in input().split(' ')]
    d = int(input())
    result = nums[d:] + nums[0:d]
    for i in range(len(result)):
        print(str(result[i]) + ' ',end='')
    print()