n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    m = i
    for j in range(i + 1, n):
        if a[j] < a[m]:
            m = j
    print(m + 1, end=" ")
    a = a[:i] + list(reversed(a[i:m + 1])) + a[m + 1:]