b_k = [int(i) for i in input().split()]
b = b_k[0]
k = b_k[1]
a = [int(i) for i in input().split()]
if b % 2 == 1:
    count_odd = 0
    for i in a:
        if i % 2 == 1:
            count_odd += 1
    if count_odd % 2 == 1:
        ans = 'odd'
    else:
        ans = 'even'
else:
    if a[k - 1] % 2 == 1:
        ans = 'odd'
    else:
        ans = 'even'

print(ans)
