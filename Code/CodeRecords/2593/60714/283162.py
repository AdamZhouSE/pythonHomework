T = int(input())
for i in range(0, T):
    n = int(input())
    base = input()
    if "," in base:
        nums = [int(x) for x in base.split(",")]
    else:
        nums = [int(x) for x in base.split()]
    temp = dict()
    for j in range(0, n):
        for k in range(j + 1, n):
            if nums[j] + nums[k] in temp:
                temp[nums[j] + nums[k]].append((j, k))
            else:
                temp[nums[j] + nums[k]] = [(j, k)]
    ans = []
    flag = False
    for item in temp:
        if len(temp[item]) >= 2:
            flag = True
            ans.append(temp[item])
    if flag:
        ans.sort()
        ans[0].sort()
        print(ans[0][0][0], ans[0][0][1], ans[0][1][0], ans[0][1][1])
    else:
        print("no pairs")
