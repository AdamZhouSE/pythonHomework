n, m, c = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
result = []
for i in range(0, n - m + 1):
    if max(nums[i:i + m]) - min(nums[i:i + m]) <= c:
        result.append(i + 1)
if len(result) == 0:
    print("NONE",end = "")
else:
    for num in result:
        print(num)
