num = int(input())
arr = input()
arr = [int(x) for x in arr.split(" ")]
vis = [0 for x in arr]
sorted(arr)
ans = 0
for i in range(num):
    if ans * (arr[i] + 1) <= i:
        ans += 1
print(ans)