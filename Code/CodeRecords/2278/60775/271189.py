
test = int(input())
for i in range(test):
    length = int(input())
    nums = [int(x) for x in input().split(' ')]
    nums.append(0)
    a2 = []
    for j in range(length):
        a2.append(nums[j] ^ nums[j+1])
    for x in a2:
        print(str(x) + ' ',end='')
