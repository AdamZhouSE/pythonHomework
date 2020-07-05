t = int(input())
for ind in range(t):
    n = int(input())
    cards = []
    haveMoved = []
    for i in range(n):
        cards.append(-1)
        haveMoved.append(False)
    i = 1
    position = 0
    while i <= n:
        count = 0
        while count < i:
            if not haveMoved[position]:
                count += 1
            position = (position + 1) % n
        while haveMoved[position]:
            position = (position+1) % n
        cards[position] = i
        haveMoved[position] = True
        position = (position + 1) % n
        i += 1
    print(*cards)
