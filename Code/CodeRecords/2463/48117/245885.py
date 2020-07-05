nums = input().split(',')
target = int(input())
realTarget = target

ans = []
end = False

for i in range(len(nums)):
    nums[i] = int(nums[i])

for i in range(len(nums)):
    if nums[i] == target:
        ans.append(i)
        ans.append(i)
        break
    else:
        if nums[i] < target:
            target -= nums[i]
            for j in range(len(nums)):
                if nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    end = True
            if end:
                break
            else:
                target = realTarget
                continue

print(ans)