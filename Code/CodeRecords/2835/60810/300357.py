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

for k in range(inp):
    if(k==2):break
    if(k!=0):
        del cards[inp-k-1]
        copy=cards
    if (int(res.join(cards)) % 90 == 0 and res == ""):
        res = "".join(cards)
    for i in range(1, fifs):
        cards[fifs - i-k] = "0"
        for j in range(fifs , inp-k):
            cards[j] = "5"
            if (int(res.join(cards)) % 90 == 0 and res == ""):
                res = "".join(cards)
                break
            cards = copy
if(res=="" and fifs==inp):
    res="-1"
elif(res=="" ):
    res="0"
print (res)
