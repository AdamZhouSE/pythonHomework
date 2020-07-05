# 17
arr = eval(input())
lower = int(input())
upper = int(input())
count = 0
for i in range(0, len(arr)):
    for j in range(i, len(arr)):
        res = sum(arr[i:j + 1])
        if upper >= res >= lower:
            count = count + 1
print(count)