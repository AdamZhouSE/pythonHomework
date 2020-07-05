cards = input().split(',')
cards = [int(x) for x in cards]
Xs = []
cards.sort()
X = 1
for i in range(len(cards) - 1):
    if cards[i] == cards[i + 1]:
        X += 1
    else:
        Xs.append(X)
        X = 1
Xs.append(X)
if max(Xs) == min(Xs) and max(Xs) >= 2:
    print('True')
elif max(Xs) % min(Xs) == 0 and min(Xs) >= 2:
    print('True')
else:
    print('False')