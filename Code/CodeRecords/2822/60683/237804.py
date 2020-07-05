n = eval(input())
src1 = [int(x) for x in input().split()]
k1 = src1[0]
src2 = [int(x) for x in input().split()]
k2 = src2[0]
card1 = src1[1:]
card2 = src2[1:]
flag = False
win = -1
ans = 0
while True:
    ans += 1
    if card1[0] > card2[0]:
        card1.append(card2[0])
        temp = card1[0]
        card1.remove(temp)
        card1.append(temp)
        card2.remove(card2[0])
        k1 += 1
        k2 -= 1
        if k2 == 0:
            flag = True
            win = 1
            break
    else:
        card2.append(card1[0])
        temp = card2[0]
        card2.remove(temp)
        card2.append(temp)
        card1.remove(card1[0])
        k2 += 1
        k1 -= 1
        if k1 == 0:
            flag = True
            win = 2
            break
    if k1 == src1[0]:
        if card1 == src1[1:]:
            break
if flag:
    temp = [str(ans), str(win)]
    print(' '.join(temp))
else:
    print(-1)