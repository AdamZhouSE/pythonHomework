li = list(eval(input().strip()))
leftMax = [li[0] for i in range(len(li)-1)]
rightMin = [li[0] for j in range(len(li)-1)]

for i in range(len(leftMax)):
    leftMax[i] = max(leftMax[i], li[i])
for j in range(len(rightMin)-1, -1, -1):
    rightMin[j] = min(rightMin[j], li[j+1])
cnt = 0
for i in range(len(leftMax)):
    if leftMax[i] <= rightMin[i]:
        cnt += 1

print(cnt+1)