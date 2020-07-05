def test():
    N = int(input())
    nums = list(map(int, input().split()))
    pos = []
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1, len(nums)):
                t = sorted([nums[i], nums[j], nums[k]])
                if t[0] + t[1] == t[2] and not t in pos:
                    pos.append(t)
    ans = len(pos)
    if ans == 0:
        ans = -1
    result.append(ans)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)