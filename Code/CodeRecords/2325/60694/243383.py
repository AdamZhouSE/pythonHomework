cards = list(map(int, input().split(",")))
setList = []
if len(cards) == 1:
    print("False")
    exit()
    
for card in cards:
    if card not in setList:
        setList.append(card)

times = []
for c in setList:
    times.append(cards.count(c))

s = set(times)
l = list(s)
if len(s) == 1 and l[0] > 1:
    print("True")
else:
    mini = min(l)
    for ele in l:
        if ele % mini != 0:
            print("False")
            exit()
    print("True")


