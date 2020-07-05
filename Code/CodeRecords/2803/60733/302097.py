n, m = map(int, input().split())
arr = [0 for l in range(m)]
for i in range(n):
    k = list(map(int, input().split()))
    for j in range(k[0]):
        if arr[k[j + 1]-1] == 0:
            arr[k[j + 1]-1] = 1
flag = 1
for i in range(m):
    if arr[i] != 1:
        flag = 0
print("YES") if flag == 1 else print("NO")

