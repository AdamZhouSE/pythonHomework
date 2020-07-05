line = input().split(" ")
length = int(line[0])
gap = int(line[1])
nums = list(map(int, input().split(" ")))
count = 1
if gap == 0:
    print(0)
else:
    for i in range(length-1):
        if nums[i+1] - nums[i] <= gap:
            count += 1
        else:
            count = 1
    print(count)
