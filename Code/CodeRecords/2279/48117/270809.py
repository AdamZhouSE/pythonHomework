questNum = int(input())

for quest in range(questNum):
    ns = input().split(' ')
    n = int(ns[0])
    s = int(ns[1])

    nums = input().split(' ')
    for i in range(n):
        nums[i] = int(nums[i])

    ans = []
    isFind = False
    for i in range(n - 1):
        res = s - nums[i]
        if res == 0:
            ans.append(i)
            ans.append(i)
            isFind = True
            break
        else:
            ans.append(i)
            for j in range(i + 1, n):
                res -= nums[j]
                if res == 0:
                    isFind = True
                    ans.append(j)
                    break
                else:
                    if res < 0:
                        isFind = False
                        break
        if not isFind:
            ans.clear()
        else:
            break
    
    if len(ans) == 0:
        print(-1)
    else:
        for k in range(len(ans)):
            if k != len(ans) - 1:
                print(ans[k] + 1, end=' ')
            else:
                print(ans[k] + 1)
