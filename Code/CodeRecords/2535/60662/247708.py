num = list(map(int, input().strip('[,]').split(',')))
l = len(num)
count = 1

leftMax = num[0]
rightMin = [0 for i in range(l)]
rightMin[l-1] = num[l-1]
i = l - 2
while i >= 0:
    if num[i] < rightMin[i+1]:
        rightMin[i] = num[i]
    else:
        rightMin[i] = num[i]
    i = i - 1

j = 1
while j < l:
    if rightMin[j] >= leftMax:
        count = count + 1
        leftMax = num[j]
    else:
        if num[j] > leftMax: 
            leftMax = num[j]
    j = j + 1
print(count)