num = int(input())
arr = input()
arr = [int(x) for x in arr.split(" ")]
res = []
sorted(arr)
arr.reverse()
vis = [0 for x in range(len(arr))]
flag = 0
for i in range(len(arr)):
    if vis[i] == -1:
        continue
    left = i
    right = i + 1
    while right < len(arr):
        if arr[left] > arr[right] and vis[right] != -1:
            vis[right] = -1
            left = right
        right += 1
    flag += 1
print(flag)
