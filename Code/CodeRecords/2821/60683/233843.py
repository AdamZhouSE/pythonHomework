n = eval(input())
cards = [int(x) for x in input().split()]
ans1 = 0
ans2 = 0
i = 0
j = n - 1
first = True
while i <= j:
    if cards[i] > cards[j]:
        if first:
            ans1 += cards[i]
            i += 1
        else:
            ans2 += cards[i]
            i += 1
    else:
        if first:
            ans1 += cards[j]
            j -= 1
        else:
            ans2 += cards[j]
            j -= 1
    first = not first
print(ans1, end=' ')
print(ans2)