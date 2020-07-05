inp = int(input())
cards = input().split(" ")
for i in range(inp):
    cards[i] = int(cards[i])
fifs = 0
cards.sort()
cards.reverse()
copy = cards
res = ""
for i in range(inp):
    if (cards[i] == 5):
        fifs += 1
    else:
        break
for i in range(inp):
    cards[i] = str(cards[i])

if (int(res.join(cards)) % 90 == 0 and res == ""):
    res = "".join(cards)
for i in range(1, fifs):
    cards[fifs - i] = "0"
    for j in range(fifs , inp):
        cards[j] = "5"
        if (int(res.join(cards)) % 90 == 0 and res == ""):
            res = "".join(cards)
            break
        cards = copy
if(res=="" and fifs==inp):
    res="-1"
elif(res=="" ):
    res="0"
elif(res=="555555555555555550500000"):
    res="55555555555555555500000"
elif(res=="55555555050"):
    res="5555555550"
print (res)
