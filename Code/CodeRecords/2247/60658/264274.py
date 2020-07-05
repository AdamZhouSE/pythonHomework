pile = [int(x) for x in input().split(",")]
i = 0
j = len(pile)-1
a = 0
b = 0
player = True
while i<=j:
    if pile[j]>pile[i]:
        if player:
            a+=pile[j]
        else:
            b+=pile[j]
        j-=1
    elif i<=j:
        if player:
            a+=pile[i]
        else:
            b+=pile[i]
        i+=1
    player = not player
print(a>b)