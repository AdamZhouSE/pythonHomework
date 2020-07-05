# 6
inp = input()
inp = input()
card = inp.split()

for i in range(len(card)):
    card[i] = int(card[i])
    
a = 0
b = 0
l = 0
r = len(card) - 1
for i in range(len(card)):
    if card[l] > card[r]:
        x = card[l]
        l = l + 1
    else:
        x = card[r]
        r = r - 1
    if i%2 == 0:
        a = a + x
    else:
        b = b + x
print(str(a) + ' ' + str(b))