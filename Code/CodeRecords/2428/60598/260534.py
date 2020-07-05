times = int(input())
for i in range(times):
    length = int(input())
    nums = list(map(int, input().split(" ")))
    tempNums = []
    ji = 0
    for j in range(length):
        if nums[j] % 2 == 0:
            tempNums.append(nums[j])
        else:
            tempNums.insert(0, nums[j])
            ji += 1
    ans = list(reversed(sorted(tempNums[0:ji])))+sorted(tempNums[ji:])
    for k in range(len(ans)-1):
        print(ans[k], "", end="")
    print(ans[len(ans)-1],"")
