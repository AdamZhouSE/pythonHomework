n=int(input())
player=[int(i) for i in input().split()]
player=list(set(player))
for i in range(0,len(player)):
    while player[i]%2==0 or player[i]%3==0:
        if player[i]%2==0:
            player[i]=int(player[i]/2)
        if player[i]%3==0:
            player[i]=int(player[i]/3)
player=list(set(player))
if len(player)==1:
    print("YES")
else:
    print("NO")