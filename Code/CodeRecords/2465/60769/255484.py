arr = list(map(int, input().split(",")))
left = 0
for i in range(len(arr)):
    if arr[-i - 1] < i:
        left = i
        break
print(arr[-left])
