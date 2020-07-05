ts = int(input())
for t in range(ts):
    n, k = map(int, input().split(' '))
    lst = list(map(int, input().split(' ')))
    max_sum = 0
    for i in range(n - k + 1):
        max_sum = max(max_sum, sum(lst[i:i + k]))
    print(max_sum)
