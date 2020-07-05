n = int(input())
nums = [int(x) for x in input().split()]
sub_seq = []
ans = []
for i in range(0, len(nums)):
    count = 0
    for j in range(0, i+1):
        try:
            ind = sub_seq.index(nums[j: i+1])
        except Exception:
            sub_seq.append(nums[j: i+1])
            count += 1
    if len(ans) == 0:
        ans.append(count)
    else:
        ans.append(ans[len(ans)-1]+count)
for i in ans:
    print(i)
