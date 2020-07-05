nums = [int(i) for i in input("")[1 : -1].split(',')]
counts = []

for i in range(0, len(nums)) :
    cnt = 0
    for j in nums[i+1 :] :
        if j < nums[i] :
            cnt += 1

    counts.append(cnt)

print(counts)
