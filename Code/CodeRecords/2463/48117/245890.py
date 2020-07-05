nums = input().split(',')
target = int(input())
realTarget = target

ans = []
end = False

for i in range(len(nums)):
    nums[i] = int(nums[i])

for i in range(len(nums)):
    if nums[i] == target:
        ans = None
        break
    else:
        if nums[i] < target:
            target -= nums[i]
            for j in range(len(nums)):
                if nums[j] == target:
                    if i == j:
                        ans = None
                    else:
                        ans.append(i + 1)
                        ans.append(j + 1)
                    end = True
            if end:
                break
            else:
                target = realTarget
                continue

print(ans)

