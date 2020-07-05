cards = list(map(int, input().split(",")))
setList = []
for card in cards:
    if card not in setList:
        setList.append(card)

times = []
for c in setList:
    times.append(cards.count(c))

s = set(times)
if len(s) == 1:
    print("True")
else:
    print("False")

