n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    op, l, r = map(int, input().split())
    if op == 0:
        arr[l-1:r] = sorted(arr[l-1:r])
    else:
        arr[l-1:r] = sorted(arr[l-1:r], reverse=True)
q = int(input())
print(arr[q-1])
