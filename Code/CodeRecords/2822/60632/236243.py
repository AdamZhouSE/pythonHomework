n = int(input())
one = list(map(int, input().split(' ')))[1:]
two = list(map(int, input().split(' ')))[1:]
i = 0
over = True
while i < len(one) and i < len(two):
    if one[i] > two[i]:
        one.append(two[i])
        one.append(one[i])
    else:
        two.append(one[i])
        two.append(two[i])
    i += 1
    if i > 100:
        print(-1)
        over = False
        break
if over:
    if len(one) > len(two):
        winner = 1
    else:
        winner = 2
    print(i, winner)