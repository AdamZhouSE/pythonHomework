def test():
    N = int(input())
    nums = list(map(int, input().split()))
    count = 0
    ans = []
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
        else:
            ans.append(str(nums[i]))
    for i in range(count):
        ans.append('0')
    result.append(' '.join(ans) + ' ')

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)