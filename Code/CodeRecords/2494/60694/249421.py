arr = eval(input())
cnt = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > 2 * arr[j]:
            cnt += 1
print(cnt)
