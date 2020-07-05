n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    op, l, r = map(int, input().split())
    if op == 0:
        arr[l:r+1].sort()
    else:
        arr[l:r+1].sort(reverse=True)
q = int(input())
print(arr[q])
