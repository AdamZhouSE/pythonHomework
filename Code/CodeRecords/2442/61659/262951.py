lists = eval(input())
lists.sort()

if len(lists) < 2:
    print(0)
else:
    gap = lists[1] - lists[0]
    for i in range(1, len(lists)):
        if (lists[i] - lists[i - 1]) > gap:
            gap = lists[i] - lists[i - 1]
    print(gap)
