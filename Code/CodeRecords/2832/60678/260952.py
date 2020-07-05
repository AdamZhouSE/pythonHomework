def biggest(nums, index):
    for i in range(0, index):
        if nums[i] > index:
            return False
    return True


n = int(input())
imfo = input().split()
for i in range(0, n):
    imfo[i] = int(imfo[i]) - 1
hope = []
for i in range(0, n):
    if imfo[i] == i:
        hope.append(i)
count = 0
for i in hope:
    if biggest(imfo, i):
        count += 1
print(count)