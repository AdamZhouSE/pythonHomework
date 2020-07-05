#06
n = int(input())
card = input().split(" ")
jal = 0
dem = 0
while len(card)>1:
    if(int(card[0])>=int(card[len(card)-1])):
        jal += int(card[0])
        card.remove(card[0])
    else:
        jal += int(card[len(card)-1])
        card.remove(card[len(card)-1])

    if (int(card[0]) >= int(card[len(card) - 1])):
        dem += int(card[0])
        card.remove(card[0])
    else:
        dem += int(card[len(card)-1])
        card.remove(card[len(card)-1])

if(len(card)==1):
    jal += int(card[0])
print(jal,end=' ')
print(dem)