def revers(l):
    return l[::-1]


n, m = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append(i + 1)
for i in range(m):
    l, r = list(map(int, input().split()))
    arr = arr[:l - 1] + revers(arr[l - 1:r]) + arr[r:]
for i in arr:
    print(i,end=" ")