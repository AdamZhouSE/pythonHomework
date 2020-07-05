times = int(input())
for i in range(times):
    length = int(input())
    Set = dict()
    nums = list(map(int, input().split(" ")))
    finish = False
    result = []
    for j in range(len(nums)):
        if nums[j] in Set:
            finish = True
            result.append(Set.get(nums[j])+1)
        else:
            Set[nums[j]] = j
    if not finish:
        print(-1)
    else:
        print(min(result))

