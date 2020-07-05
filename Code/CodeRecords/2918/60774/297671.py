n = int(input())
press = list(map(int,input().split(' ')))
press.sort()
piles = [1]
for i in range(1,n):
    for j in range(0,len(piles)):
        if(press[i] >= piles[j]):
            piles[j] = piles[j] + 1
            break
    else:
        piles.append(1)
print(len(piles))