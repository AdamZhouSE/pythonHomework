ts = int(input())
for t in range(ts):
    n = int(input())
    lst = list(map(int, input().split(' ')))
    for i in range(2, len(lst)):
        lst[i] += min(lst[i - 1], lst[i - 2])
    print(min(lst[-1], lst[-2]))
