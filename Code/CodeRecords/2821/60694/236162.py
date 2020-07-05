num = int(input())
x = input()
xList = x.split(" ")
cards = [int(xList[i]) for i in range(len(xList))]

scoreA = 0
scoreB = 0


for i in range(num):
    if i % 2 == 0:  # A's turn
        if cards[0] > cards[len(cards) - 1]:
            scoreA += cards[0]
            del cards[0]
        else:
            scoreA += cards[len(cards) - 1]
            del cards[len(cards) - 1]

    else:  # B's turn
        if cards[0] > cards[len(cards) - 1]:
            scoreB += cards[0]
            del cards[0]
        else:
            scoreB += cards[len(cards) - 1]
            del cards[len(cards) - 1]

print(str(scoreA) + " " + str(scoreB))
