n = int(input())
list_num = [int(i) for i in input().split()]
list_neg = []
list_pos = []
list_zero = []
ans = 0
for i in list_num:
    if i < 0:
        list_neg.append(i)
    elif i > 0:
        list_pos.append(i)
    else:
        list_zero.append(i)
if len(list_neg) % 2 == 1:
    if len(list_zero) > 0:
        for i in list_neg:
            ans += ((-1) - i)
        ans += len(list_zero)
        for i in list_pos:
            ans += (i - 1)
    else:
        for i in list_neg:
            ans += ((-1) - i)
        max_neg = max(list_neg)
        ans -= (-1 - max_neg)
        ans += (1 - max_neg)
        for i in list_pos:
            ans += (i - 1)
else:
    for i in list_neg:
        ans += ((-1) - i)
    ans += len(list_zero)
    for i in list_pos:
        ans += (i - 1)
print(ans)