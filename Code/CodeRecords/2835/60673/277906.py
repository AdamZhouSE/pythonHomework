inp = int(input())
cards = input().split(" ")
for i in range(inp):
    cards[i] = int(cards[i])
fifs = 0
cards.sort()
cards.reverse()
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
    for j in range(fifs - 1, inp):
        cards[j] = "5"
        cards[fifs - 1 - i] = "0"
        if (int(res.join(cards)) % 90 == 0 and res == ""):
            res = "".join(cards)
            break
if(res=="" and fifs==inp):
    res="-1"
elif(res=="" ):
    res="0"
print (res)
