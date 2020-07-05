input()
cards = [int(x) for x in input().split()]
i, j = [0, len(cards) - 1]
ans1 = 0
ans2 = 0
for x in range(0, len(cards)):
    if x % 2 is 0:
        if cards[i] > cards[j]:
            ans1 += cards[i]
            i += 1
        else:
            ans1 += cards[j]
            j -= 1
    else:
        if cards[i] > cards[j]:
            ans2 += cards[i]
            i += 1
        else:
            ans2 += cards[j]
            j -= 1
print(ans1, ans2)
