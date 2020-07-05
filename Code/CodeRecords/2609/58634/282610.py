t = int(input())
for _ in range(t):
    n, k = map(int, input().split(" "))
    nums = list(map(int, input().split(" ")))
    new_nums = []
    for i in nums:
        if nums.count(i)>1:
            continue
        else:
            new_nums.append(i)
    print(new_nums[k-1]) if k-1<len(new_nums) else print(-1)
