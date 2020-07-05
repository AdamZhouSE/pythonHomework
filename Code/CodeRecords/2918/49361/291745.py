num = int(input())
arr = input()
arr = [int(x) for x in arr.split(" ")]
sorted(arr)
ans = 0
for i in range(num):
    if ans * (arr[i] + 1) <= i:
        ans += 1
print(ans)