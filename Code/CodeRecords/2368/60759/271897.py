ts = int(input())
for t in range(ts):
    n = int(input())
    lst = input().split(' ')
    ans = []
    is_max = True
    while len(lst) > 0:
        if is_max:
            ans.append(lst.pop())
        else:
            ans.append(lst.pop(0))
        is_max = not is_max
    print(' '.join(ans) + ' ')
