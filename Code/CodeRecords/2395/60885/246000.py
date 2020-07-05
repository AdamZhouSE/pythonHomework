def test():
    N = int(input())
    nums = list(map(int, input().split())) + [0]
    count = 0
    ans = []
    for i in range(len(nums)-1):
        if nums[i] == 0:
            count += 1
        elif nums[i+1] != 0 and nums[i] == nums[i+1]:
            ans.append(str(nums[i]*2))
            nums[i+1] = 0
        else:
            ans.append(str(nums[i]))
    for i in range(count):
        ans.append('0')
    result.append(' '.join(ans))

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)